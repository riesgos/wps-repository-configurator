#!/bin/sh

cd project
rm -rf /var/www/static || echo 'skip'
mkdir /var/www/static
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver 0.0.0.0:8000
