#!/bin/bash

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn sola.wsgi:application -w 3 --bind 0.0.0.0:8000
