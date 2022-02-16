# table-games-library
Family Table Games Library

## install
1. git clone git@github.com:ILLIDOM/table-games-library.git
2. create venv ``virtualenv --python=3.10 venv``
3. install requirements ``pip install -r requirements.txt``

## running app
- for dev use ``python wsgi.py``
- for prod use ``gunicorn -b <ip>:<port> --workers <num> wsgi:app``