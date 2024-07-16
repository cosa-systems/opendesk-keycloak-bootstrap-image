#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023 Bundesministerium des Innern und für Heimat, PG ZenDiS "Projektgruppe für Aufbau ZenDiS"
# SPDX-License-Identifier: Apache-2.0

import sys
import yaml
import logging
from lib.keycloak import Keycloak

logging.basicConfig(format='%(asctime)s %(levelname)-5.5s: %(message)s', level=logging.NOTSET)
logging.info("Initializing basic parameters")

with open('/app/values.yaml', 'r') as file:
    config = yaml.safe_load(file)

KEYCLOAK_ADMUSER = config['config']['keycloak']['adminUser']
KEYCLOAK_ADMPASS = config['config']['keycloak']['adminPassword']
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
    keep_names = []
    for section in [ 'opendesk', 'custom' ]:
        if type in config['config'][section]:
            type_config = config['config'][section][type]
            logging.info(f"Processing {type} from {section}")
            for object in type_config:
                if 'name' not in object:
                    sys.exit(f"! 'name' attribute is mandatory for objects but missing: {object}")
                keep_names.append(object['name'])
                logging.info(f"Working on {type}: {object['name']}")
                kc.create_or_recreate_object(type=type, data=object)
        else:
            logging.debug(f"No {type} found in {section}.")
        kc.reconcile_objecttype(type=type, keep_names=keep_names)
