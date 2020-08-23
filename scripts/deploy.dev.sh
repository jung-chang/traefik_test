#! /usr/bin/env bash

# Exit in case of error
set -e

# xargs removes whitespace
export HOST_IP=$(hostname -I | xargs)

docker-compose -f docker-compose.yml up --build --force-recreate