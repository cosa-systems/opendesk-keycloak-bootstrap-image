# SPDX-FileCopyrightText: 2024-2025 Zentrum für Digitale Souveränität der Öffentlichen Verwaltung (ZenDiS) GmbH
# SPDX-FileCopyrightText: 2023 Bundesministerium des Innern und für Heimat, PG ZenDiS "Projektgruppe für Aufbau ZenDiS"
# SPDX-License-Identifier: Apache-2.0

FROM registry-1.docker.io/library/alpine:3.20.2

WORKDIR /app

RUN apk add --no-cache \
    python3=3.12.9-r0 \
    py3-pip=24.0-r2 \
    py3-jmespath=1.0.1-r3 \
    py3-requests=2.32.3-r0 \
    ansible=9.5.1-r0 \
    bash=5.2.26-r0 \
  && addgroup -S "app" \
  && adduser -D -G "app" -h "/app" -s "/bin/bash" -u 1000 -S "app"

USER app

COPY bootstrap-opendesk-keycloak /app

CMD ["/bin/bash", "-c", "/app/entrypoint.sh"]
