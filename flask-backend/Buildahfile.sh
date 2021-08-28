#!/usr/bin/env bash

set -o errexit

FLASK_ROOT="/opt/api"
FLASK_USER="www-data"
USER_ID="1000"
FLASK_USER_ID="${USER_ID}"
VENV_NAME=".venv-docker"

# Create a container
CONTAINER=$(buildah from docker.io/python:3.7-buster)
# Labels are part of the "buildah config" command
buildah config --label maintainer="Angel Rey <afreydev@gmail.com>" "$CONTAINER"
buildah run "$CONTAINER" -- sh -c """
apt-get update && apt-get install -y \
build-essential python3-dev python3-pip python3-venv && \
rm -rf /var/lib/apt/lists/*
"""

buildah config --workingdir "$FLASK_ROOT" "$CONTAINER"
buildah copy "$CONTAINER" 'api/requirements.txt' "$FLASK_ROOT/requirements.txt"
buildah run "$CONTAINER" -- pip install virtualenv
buildah run "$CONTAINER" -- virtualenv "/opt/$VENV_NAME"
buildah config --env PATH="/opt/${VENV_NAME}/bin:\${PATH}" "$CONTAINER"
buildah run "$CONTAINER" -- sh -c "pip install -r requirements.txt && rm requirements.txt"
buildah run "$CONTAINER" -- sh -c """
    userdel $FLASK_USER && addgroup --system --gid $FLASK_USER_ID $FLASK_USER && \
    adduser --system --uid $FLASK_USER_ID --no-create-home --ingroup $FLASK_USER --shell /bin/false $FLASK_USER
"""

buildah run "$CONTAINER" -- sh -c """
    chown -R $FLASK_USER_ID:$FLASK_USER_ID /opt/$VENV_NAME/
"""

buildah copy "$CONTAINER" 'api' "$FLASK_ROOT"
buildah config --user "$FLASK_USER" "$CONTAINER"
buildah config --cmd "bash run.sh" "$CONTAINER"

# Finally saves the running container to an image
buildah commit --format docker "$CONTAINER" flask-backend:latest