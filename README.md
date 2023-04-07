# FastAPI + SQLAlchemy Boilerplate

This project is intended to be used as a sample/boilerplate for how to set up FastAPI with SQLAlchemy

## Getting started

1. Start a python virtualenv: `python -m venv venv`
2. Install python dependencies: `pip install -r requirements.txt`
3. Start PostgreSQL database with Docker (ensure Docker is installed): `invoke start_database`
4. Run migrations: `invoke run_migrations`
   1. Note: You can wipe out everything in the DB whenever with the following command: `invoke undo_migrations`
5. Start the server: `invoke run`

## Other concepts to know

1. Tests: `invoke test`
2. Migrations:
3. Seeding data
