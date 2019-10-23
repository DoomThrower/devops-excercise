#!/usr/bin/env bash

set -x
# Insert age
curl -H "Host: db.docker.localhost" -X PUT -H "Content-Type: application/json" -d @data.json http://localhost/age
# Get age list
curl -H "Host: db.docker.localhost" localhost/age/Lukas

# Sample commands for parallel curling
#seq 4 | parallel -n0 -j2 "curl -H 'Host: cpu.docker.localhost' localhost/local_program"
#seq 100000 | parallel -j0 --joblog log "curl -H 'Host: cpu.docker.localhost' localhost/local_program" ">" {}.txt
#cut -f 4 log