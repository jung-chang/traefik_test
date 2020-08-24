#! /usr/bin/env bash

# Exit in case of error
set -e

# xargs removes whitespace
export HOST_IP=172.17.0.1
export HOST_IP=$(hostname -I | xargs)

docker-compose -f docker-compose.prod.yml up --build --force-recreate