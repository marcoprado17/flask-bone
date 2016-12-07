#!/usr/bin/env bash

cd /vagrant;
gunicorn build:app -b localhost:8000;