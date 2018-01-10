#!/bin/bash

rm -fr example/__pycache__
rm -fr store/__pycache__
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations store
python manage.py migrate store
python attempt.py