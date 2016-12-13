#!/usr/bin/env bash

SHARED_SERVER_SETUP_FULL_PATH=/vagrant/scripts/server_setups/shared.sh;
SET_TIMEZONE_FULL_PATH=/vagrant/scripts/server_setups/set_timezone.sh;

chmod +x ${SHARED_SERVER_SETUP_FULL_PATH};
${SHARED_SERVER_SETUP_FULL_PATH};
chmod -x ${SHARED_SERVER_SETUP_FULL_PATH};

chmod +x ${SET_TIMEZONE_FULL_PATH};
${SET_TIMEZONE_FULL_PATH};
chmod -x ${SET_TIMEZONE_FULL_PATH};