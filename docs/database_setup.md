# DB - PostgreSQL
1. Run postgresql in container ``docker run --name some-postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:14``
2. Connec to to shell of container
3. open psql shell ``psql -U postgres``
4. create db ``CREATE DATABASE table_game_libarary;``

# DB - Sqlite
1. run flask db commands (init, migrate, upgrade) -> creates new empty db with correct schema
2. fill in dummy data

## query tables
- ``\l`` list all databases
- ``\dt`` see all tables
- ``\d <table-name>`` see table structure
- query users: ``select * from public.user;`` important to use public because .user is also an internal table

## DB Migrations / Upgrade
1. init flask-migrate ``flask db init``
2. migrate schema ``flask db migrate -m "message"``
3. upgrade db to new schema ``flask db upgrade``

## Backup/Restore Database (psql)
1. Dump into file on local machine from docker container: 
``docker exec -i pg_container_name /bin/bash -c "PGPASSWORD=pg_password pg_dump --username pg_username database_name" > /desired/path/on/your/machine/dump.sql``
2. Backup dump into container
``docker exec -i pg_container_name /bin/bash -c "PGPASSWORD=pg_password psql --username pg_username database_name" < /path/on/your/machine/dump.sql``
