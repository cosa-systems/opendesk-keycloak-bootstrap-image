#!/bin/bash
# SPDX-FileCopyrightText: 2023 Bundesministerium des Innern und für Heimat, PG ZenDiS "Projektgruppe für Aufbau ZenDiS"
# SPDX-License-Identifier: Apache-2.0

# Exit on the first command returning with an RC >0
set -e

# Convention over configuration, this is the Ansible playbook that gets started when available.
ANSIBLE_ENTRYPOINT=/app/ansible/main.yml

# Optional debug pause
regex_check_int='^[0-9]+$'
if [[ $OPENDESK_KEYCLOAK_BOOTSTRAP_DEBUG_PAUSE_BEFORE_SCRIPT_START =~ $regex_check_int ]] ; then
  echo "- Pausing $OPENDESK_KEYCLOAK_BOOTSTRAP_DEBUG_PAUSE_BEFORE_SCRIPT_START seconds before starting the script."
  sleep $OPENDESK_KEYCLOAK_BOOTSTRAP_DEBUG_PAUSE_BEFORE_SCRIPT_START
fi

# Process the custom objects
/app/keycloak-config-object-manager/kcom.py

## Bootstrap aditionally based on custom directories created by configMaps
if [[ -f "${ANSIBLE_ENTRYPOINT}" ]]; then
  export ANSIBLE_HOME=$OPENDESK_KEYCLOAK_BOOTSTRAP_TEMP_DIR
  export ANSIBLE_REMOTE_TMP=$OPENDESK_KEYCLOAK_BOOTSTRAP_TEMP_DIR
  cd $OPENDESK_KEYCLOAK_BOOTSTRAP_TEMP_DIR
  echo "- Found ${ANSIBLE_ENTRYPOINT} and starting it now..."
  ansible-playbook -v "${ANSIBLE_ENTRYPOINT}"
fi

