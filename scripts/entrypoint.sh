#!/bin/bash

python manage.py migrate --noinput
gunicorn sola.wsgi:application -w 1 --bind 0.0.0.0:8000
