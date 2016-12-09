#!/usr/bin/env bash

SHARED_SERVER_SETUP_FULL_PATH=/vagrant/scripts/server_setups/shared.sh;

chmod +x ${SHARED_SERVER_SETUP_FULL_PATH};
$SHARED_SERVER_SETUP_FULL_PATH;
chmod -x ${SHARED_SERVER_SETUP_FULL_PATH};

sudo mkdir /vagrant/configs/instance;
sudo touch /vagrant/configs/instance/config.py;
echo "DEBUG=False" >> /vagrant/configs/instance/config.py;
echo "STATIC_FOLDER=None" >> /vagrant/configs/instance/config.py;

sudo apt-get install -y python nginx gunicorn;
sudo /etc/init.d/nginx start;
sudo rm /etc/nginx/sites-enabled/default;
sudo rm /etc/nginx/sites-available/src;
sudo rm /etc/nginx/sites-enabled/src;
sudo cp /vagrant/configs/ngix_config /etc/nginx/sites-available/src;
sudo ln -s /etc/nginx/sites-available/src /etc/nginx/sites-enabled/src;
sudo /etc/init.d/nginx restart;