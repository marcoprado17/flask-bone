#!/usr/bin/env bash

gunicorn /vagrant/build:app -b localhost:8000;