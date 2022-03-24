#!/usr/bin/env bash
# Setting up configs to serve web static




apt-get update -y
apt-get install nginx -y 
mkdir -p "/data/web_static/releases/test/"
mkdir "data/web_static/shared"

