#!/usr/bin/env bash

cd /vagrant;
gunicorn src.wsgi:app -b localhost:8000;