from invoke import task


@task
def install(c):
    c.run("pip install -r requirements.txt")


@task
def run(c):
    c.run("uvicorn app.main:app --reload --port 9090")


@task
def test(c):
    c.run("pytest")

@task
def run_migrations(c):
    c.run("alembic upgrade head")

@task
def undo_migrations(c):
    c.run("alembic downgrade base")

@task
def create_database(c):
    c.run("docker run --name fastapi-sqlalchemy-db -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=user_db -p 5432:5432 -d postgres")
