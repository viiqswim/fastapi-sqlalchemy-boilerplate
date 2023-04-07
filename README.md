# FastAPI + SQLAlchemy Boilerplate

This project is intended to be used as a sample/boilerplate for how to set up FastAPI with SQLAlchemy

## Getting started

1. Start a python virtualenv: `python -m venv venv`
2. Install python dependencies: `pip install -r requirements.txt`
3. Start PostgreSQL database with Docker (ensure Docker is installed): `invoke start-database`
4. Run migrations: `invoke run-migrations`
   1. Note: You can wipe out everything in the DB whenever with the following command: `invoke undo-migrations`
5. Start the server: `invoke run`

## Other concepts to know

1. Tests: `invoke test`
2. Migrations
3. Seeding data
   1. Add seed data: `invoke seed`
   2. Remove all data: `invoke clear-data`

## Notes

1. When creating the database (`invoke start-database`) command, you can modify the database name, username, and password: `invoke start-database --database_name="replace_me" --username="replace_me" --username="replace_me"`
