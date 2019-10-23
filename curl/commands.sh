#!/usr/bin/env bash

set -x
# Insert age
curl -X PUT -H "Content-Type: application/json" -d @data.json http://localhost:8080/age
# Get age list
curl localhost:8080/age/Lukas