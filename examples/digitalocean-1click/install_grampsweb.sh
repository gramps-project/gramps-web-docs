#!/usr/bin/env bash

# fail on errors
set -eu

# disable user interactions
export DEBIAN_FRONTEND="noninteractive"

# install docker and the compose plugin from Docker's repository
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc
cat > /etc/apt/sources.list.d/docker.sources <<EOM
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOM
apt-get -qq update
apt-get -qq install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
systemctl enable docker

# run the first-login wizard on the first interactive root login
cat >> /root/.bashrc <<EOM
/opt/grampsweb/firstlogin.sh
EOM

# clear package cache
apt-get -qq autoclean
apt-get -qq autoremove
