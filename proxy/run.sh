#!/bin/sh

# ako ijedna komanda padne, pada citava skripta
set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'
