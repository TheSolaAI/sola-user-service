#!/bin/bash

gunicorn sola.wsgi:application -w 1 --bind 0.0.0.0:8000
