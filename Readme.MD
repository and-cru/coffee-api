# Coffee API

> Simple CRUD API to create coffee brew recipes

API was built with [FastAPI](https://fastapi.tiangolo.com/)

## How it works

All you need is a running [Docker](https://docs.docker.com/get-docker/) daemon. Then simply run the below:

```bash
docker-compose up -d --build
```

This will build and bring up the services for the CRUD API. Confirm that the app is up by accessing:

`http://localhost:8080/health` -> Returns an I am healthy message

Access the docs for the API by going to `http://localhost:8080/docs`

## Migrations

Using [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment), we can easily run DB migrations. To run a new migration follow the below:

Navigate into `src`

```bash
cd src/
```

Then run Alembic revision command:

```bash
alembic revision -m 'My new migration'
```

This will generate a new migration file inside the `coffee/version`, edit this file and added the DB chnages.

For the changes to take effect, run:

```bash
cd .. && docker-compose down && docker-compose up -d --build
```