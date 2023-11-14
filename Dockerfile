# SPDX-FileCopyrightText: 2023 Bundesministerium des Innern und für Heimat, PG ZenDiS "Projektgruppe für Aufbau ZenDiS"
# SPDX-License-Identifier: Apache-2.0

FROM external-registry.souvap-univention.de/sovereign-workplace/alpine:3.18.4

WORKDIR /app

RUN apk add \
    python3 \
    py3-pip \
    ansible \
    bash \
  && addgroup -S "app" \
  && adduser -D -G "app" -h "/app" -s "/bin/bash" -u 1000 -S "app"

USER app

ADD bootstrap-opendesk-keycloak /app

# Add Python script requirements
RUN pip install -r /app/keycloak-config-object-manager/requirements.txt

# Ansible requirements
RUN pip install jmespath

CMD ["/bin/bash", "-c", "/app/entrypoint.sh"]
