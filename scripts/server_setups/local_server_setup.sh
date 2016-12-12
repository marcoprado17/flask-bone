#!/usr/bin/env bash

SHARED_SERVER_SETUP_FULL_PATH=/vagrant/scripts/server_setups/shared.sh;

chmod +x ${SHARED_SERVER_SETUP_FULL_PATH};
${SHARED_SERVER_SETUP_FULL_PATH};
chmod -x ${SHARED_SERVER_SETUP_FULL_PATH};