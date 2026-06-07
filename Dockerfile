# SPDX-FileCopyrightText: 2024-2026 Zentrum für Digitale Souveränität der Öffentlichen Verwaltung (ZenDiS) GmbH
# SPDX-FileCopyrightText: 2023 Bundesministerium des Innern und für Heimat, PG ZenDiS "Projektgruppe für Aufbau ZenDiS"
# SPDX-License-Identifier: Apache-2.0

FROM docker.io/alpine:3.23.3

WORKDIR /app

RUN apk add --no-cache \
    python3=3.12.13-r0 \
    py3-pip=25.1.1-r1 \
    py3-jmespath=1.0.1-r4 \
    py3-requests=2.33.1-r0 \
    ansible=13.0.0-r0 \
    bash=5.3.3-r1 \
  && addgroup -S "app" \
  && adduser -D -G "app" -h "/app" -s "/bin/bash" -u 1000 -S "app"

USER app

COPY bootstrap-opendesk-keycloak /app

CMD ["/bin/bash", "-c", "/app/entrypoint.sh"]
