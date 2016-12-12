#!/usr/bin/env bash

cd /vagrant;
gunicorn build.wsgi:app -b localhost:8000;