#!/bin/sh

# run first login wizard
/opt/grampsweb/firstlogin.py

# restore default bashrc file
cp -f /etc/skel/.bashrc /root/.bashrc

# start services using docker-compose
(cd /opt/grampsweb && docker compose pull && docker compose stop && docker compose up --remove-orphans -d)
