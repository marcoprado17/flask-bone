#!/usr/bin/env bash

SHARED_SERVER_SETUP_FULL_PATH=/vagrant/scripts/server_setups/shared.sh

chmod +x $SHARED_SERVER_SETUP_FULL_PATH
(exec "$SHARED_SERVER_SETUP_FULL_PATH")
chmod -x $SHARED_SERVER_SETUP_FULL_PATH