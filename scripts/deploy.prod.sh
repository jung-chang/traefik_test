#! /usr/bin/env bash

# Exit in case of error
set -e

# xargs removes whitespace
export HOST_IP=172.17.0.1

docker-compose -f docker-compose.prod.yml up --build --force-recreate