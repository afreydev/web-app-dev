#!/bin/bash
set -e
./Buildahfile.sh
PODMAN_NETWORK="companies_network"
DB_CONTAINER_NAME="companies_mariadb"
FLASK_CONTAINER_NAME="companies"

# Cleaning things
# podman stop companies_mariadb
# podman rm companies_mariadb
# podman stop companies
# podman rm companies
# podman network rm companies_network

podman network create "$PODMAN_NETWORK"
podman run -d --restart=always --env-file=.env --network="$PODMAN_NETWORK" --name="$DB_CONTAINER_NAME" mariadb
DB_HOST=$(podman inspect --format "{{ .NetworkSettings.Networks.$PODMAN_NETWORK.IPAddress }}" $DB_CONTAINER_NAME)
sed -i "s/MYSQL_HOST.*/MYSQL_HOST=$DB_HOST/" .env
podman run -d --restart=always --env-file=.env -p 8080:5000 --network="$PODMAN_NETWORK" --name="$FLASK_CONTAINER_NAME" localhost/flask-backend:latest
