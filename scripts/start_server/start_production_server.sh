#!/usr/bin/env bash

cd /vagrant;
gunicorn build.apps_holder:app -b localhost:8000;