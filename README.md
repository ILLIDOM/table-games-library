# table-games-library
Family Table Games Library

## install
1. git clone git@github.com:ILLIDOM/table-games-library.git
2. create venv ``virtualenv --python=3.10 venv``
3. activate venv ``source venv/bin/activate``
3. install requirements ``pip install -r src/requirements.txt``

## running app
- for dev use ``python wsgi.py``
- for prod use ``gunicorn -b <ip>:<port> --workers <num> wsgi:app``

## testing app
- run ``python -m pytest -v`` inside src folder

## build docker image
- ``docker build -t dominique123456789/tlg-flask .``
