#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024-2025 Zentrum für Digitale Souveränität der Öffentlichen Verwaltung (ZenDiS) GmbH
# SPDX-FileCopyrightText: 2023 Bundesministerium des Innern und für Heimat, PG ZenDiS "Projektgruppe für Aufbau ZenDiS"
# SPDX-License-Identifier: Apache-2.0

import sys
import yaml
import logging
from lib.keycloak import Keycloak

logging.basicConfig(format='%(asctime)s %(levelname)-5.5s: %(message)s', level=logging.NOTSET)
logging.info("Initializing basic parameters")

# Read the secret-resolved values written by provisionValuesYaml.py (/tmp/values.yaml),
# not the raw mounted /app/values.yaml — otherwise unresolved `existingSecret` blocks are
# sent to Keycloak verbatim (HTTP 400 on client create). entrypoint.sh runs
# provisionValuesYaml.py before this, so /tmp/values.yaml always exists here.
with open('/tmp/values.yaml', 'r') as file:
    config = yaml.safe_load(file)

with open('/app/admin.yaml', 'r') as file:
    admin = yaml.safe_load(file)

KEYCLOAK_ADMUSER = admin['username']
KEYCLOAK_ADMPASS = admin['password']
KEYCLOAK_USER_REALM = config['config']['keycloak']['realm']
if config['config']['keycloak']['intraCluster']['enabled']:
    KEYCLOAK_BASE_URL = config['config']['keycloak']['intraCluster']['internalBaseUrl']
else:
    KEYCLOAK_BASE_URL = 'https://'+config['global']['hosts']['keycloak']+'.'+config['global']['domain']

kc = Keycloak(
    adm_username=KEYCLOAK_ADMUSER,
    adm_password=KEYCLOAK_ADMPASS,
    realm=KEYCLOAK_USER_REALM,
    base_url=KEYCLOAK_BASE_URL
)

# We enforce a certain order, as clientScopes should always be processed before clients.
# We already recreate these objects to ensure they are in line with the provided config.
for type in ['clientScopes', 'clients']:
    keep_names = config['config']['managed'][type]
    for section in [ 'opendesk', 'custom' ]:
        if type in config['config'][section]:
            logging.info(f"Processing {type} from {section}")
            type_config = config['config'][section][type]
            for key in type_config:
                if 'name' not in type_config[key]:
                    sys.exit(f"! 'name' attribute is mandatory for objects but missing: {type_config[key]}")
                keep_names.append(type_config[key]['name'])
                logging.info(f"Working on {type}: {key}")
                kc.create_or_recreate_object(type=type, data=type_config[key])
        else:
            logging.debug(f"No {type} found in {section}.")
        kc.reconcile_objecttype(type=type, keep_names=keep_names)
