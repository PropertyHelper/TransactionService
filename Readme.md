# About
A service to manage transactions. Find details in [yandex wiki](https://wiki.yandex.ru/facesmile/transaction-service-design/).
# How to run
1. Create a file .postgres.env and put there
``POSTGRES_PASSWORD=<password>``, where `<password>` is the desired password for docker database.
2. Create a file .env and put there `db_connection_str=postgresql+asyncpg://<user>:<password>@<host>>:<port>>/postgres`.
If you run using Docker Compose (default), set the db_connection_str to `db_connection_str=postgresql+asyncpg://postgres:<password>@db:5432/postgres`,
and change `<password>` to password created at p.1
3. Issue `docker compose build`
4. Issue `docker compose up`
# After execution
use `docker compose down`. Note that the database creates a volume.