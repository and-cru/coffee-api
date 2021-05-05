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

## Connect to pgAdmin4

To view the DB, open [Chrome](https://www.pgadmin.org/faq/) as limited browsers are supported, then navigate to `localhost:16543/` and login with `username: admin@admin.com` & `password: test123!`

Thereafter click on server -> create new server. Give the server a `name`, to find the hostname run:

```bash
ifconfig |grep inet
```

There will be an IP for our Docker network, use that as the hostname. The rest is simple, DB username and password is both `postgres`

## To-do:

- [ ] Update method - [Pydantic](https://pydantic-docs.helpmanual.io/usage/exporting_models/#modeljson) & [Example](https://github.com/tiangolo/full-stack-fastapi-postgresql/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/app/crud/crud_user.py)