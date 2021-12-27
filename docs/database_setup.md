# DB
1. Run postgresql in container ``docker run --name some-postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:14``
2. Connec to to shell of container
3. open psql shell ``psql -U postgres``
4. create db ``CREATE DATABASE table_game_libarary;``

## query tables
- ``\dt`` see all tables
- ``\d <table-name>`` see table structure
- query users: ``select * from public.user;`` important to use public because .user is also an internal table

## DB Migrations / Upgrade
1. init flask-migrate ``flask db init``
2. migrate schema ``flask db migrate -m "message"``
3. upgrade db to new schema ``flask db upgrade``