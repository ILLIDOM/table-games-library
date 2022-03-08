# table-games-library
Family Table Games Library

## install
1. git clone git@github.com:ILLIDOM/table-games-library.git
2. create venv ``virtualenv --python=3.10 venv``
3. activate vend ``source venv/bin/activate``
3. install requirements ``pip install -r application/requirements.txt``

## running app
- for dev use ``python wsgi.py``
- for prod use ``gunicorn -b <ip>:<port> --workers <num> wsgi:app``

## build docker image
- ``docker build -t dominique123456789/tlg-flask .``