# SPDX-FileCopyrightText: 2024 Zentrum für Digitale Souveränität der Öffentlichen Verwaltung (ZenDiS) GmbH
# SPDX-FileCopyrightText: 2023 Bundesministerium des Innern und für Heimat, PG ZenDiS "Projektgruppe für Aufbau ZenDiS"
# SPDX-License-Identifier: Apache-2.0

FROM registry-1.docker.io/library/alpine:3.19.1

WORKDIR /app

RUN apk add \
    python3=3.11.9-r0 \
    py3-pip=23.3.1-r0 \
    py3-jmespath=1.0.1-r1 \
    py3-deepdiff=6.7.1-r0 \
    py3-requests=2.31.0-r1 \
    ansible=8.6.1-r0 \
    bash=5.2.21-r0 \
  && addgroup -S "app" \
  && adduser -D -G "app" -h "/app" -s "/bin/bash" -u 1000 -S "app" \
  && rm -vrf /var/cache/apk/*

USER app

ADD bootstrap-opendesk-keycloak /app

CMD ["/bin/bash", "-c", "/app/entrypoint.sh"]
