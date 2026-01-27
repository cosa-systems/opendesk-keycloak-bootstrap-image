<!--
SPDX-FileCopyrightText: 2026 Zentrum für Digitale Souveränität der Öffentlichen Verwaltung (ZenDiS) GmbH
SPDX-FileCopyrightText: 2023 Bundesministerium des Innern und für Heimat, PG ZenDiS "Projektgruppe für Aufbau ZenDiS"
SPDX-License-Identifier: Apache-2.0
-->

# openDesk Keycloak Bootstrap Container Image

This image is used by the openDesk Keycloak Bootstrap Helm Chart to bootstrap the Keycloak configuration for openDesk based on an base configuration of an Univention Keycloak.

## Getting Started

The image that is build by this repository's contents should only be used in conjunction with the related Helm Chart.
It is therefore tested with Kubernetes deployments only. Though you can make use of the image in stand alone
container environments for debugging purposes.

## Contents

The values from the Helm Chart have to be made available to the image in `/app/values.yaml`.

### Python script: `provisionValuesYaml.py`

A small script that injects or replaces confidential values in the configuration of a client object or the SSO Federation. Those values have to be provided in the `/app/secrets` folder as a file according to the pattern: `existingSecret.name-existingSecret.key` and supersede the `value` on the same level as the `existingSecret`.

### Python script: `kcom.py` (Keycloak Object Manager)

A simple script for the configuration, update and removal of certain Keycloak objects based on their yaml representation
of these objects. Currently supported object types:
- Client Scopes
- Clients

### Ansible playbook: `main.yaml`

Optionally you can mount the directory `/app/ansible` where the image will look up for a `main.yml` in order to start is
as `ansible-playbook`. The ansible temporary dir is set to `/tmp`.

## Environment variables

The following environment variables are supported:

- `OPENDESK_KEYCLOAK_BOOTSTRAP_DEBUG_PAUSE_BEFORE_SCRIPT_START`: When set to a positiv integer value it will pause the
  execution of the `entrypoint.sh` script which can be convenient in debugging scenarios.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## License

This project uses the following license: Apache-2.0

## Copyright

Copyright © 2026 Zentrum für Digitale Souveränität der Öffentlichen Verwaltung (ZenDiS) GmbH
