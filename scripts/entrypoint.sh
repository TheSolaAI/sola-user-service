#!/bin/bash

python manage.py migrate --noinput
gunicorn sola.wsgi:application -w 3 --bind 0.0.0.0:8000
