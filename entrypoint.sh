#!/bin/bash

# create db schema 
#flask db init
#flask db migrate
#flask db upgrade

gunicorn -b 0.0.0.0:5000 wsgi:app