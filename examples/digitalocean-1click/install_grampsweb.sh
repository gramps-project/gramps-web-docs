#!/usr/bin/env bash

# fail on errors
set -eu

# Add first-login task
cat >> /root/.bashrc <<EOM
/opt/grampsweb/firstlogin.sh
EOM

# disable user interactions
export DEBIAN_FRONTEND="noninteractive"
export TMPDIR="/tmp"

# update operating system
apt-get update
apt dist-upgrade 2>/dev/null

# install dependencies
apt-get -qq install --no-install-recommends apt-transport-https ca-certificates \
        curl software-properties-common openssl

# install docker if needed
if ! command -v docker &> /dev/null; then
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/trusted.gpg.d/download.docker.com.gpg
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable"
  apt-get update
  apt-get -qq install docker-ce
fi

# install docker-compose if needed
if ! command -v docker-compose &> /dev/null; then
  apt-get update
  apt-get -qq install docker-compose-plugin
fi

# create user
useradd -o -m -U -u 1000 -G docker -d /opt/grampsweb grampsweb || echo "User 'grampsweb' already exists. Proceeding."
mkdir -p /opt/grampsweb/media

# change permissions
chown -Rf grampsweb:grampsweb /opt/grampsweb

# clear package cache
apt-get autoclean
apt-get autoremove
