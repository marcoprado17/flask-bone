#!/usr/bin/env bash

sudo apt-get update;
sudo apt-get install -y python-pip;
sudo apt-get install -y python-dev;

sudo pip install -r /vagrant/requirements.txt