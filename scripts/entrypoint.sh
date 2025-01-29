#!/bin/bash

python manage.py migrate --noinput
gunicorn sola.wsgi:application --bind 0.0.0.0:8000
