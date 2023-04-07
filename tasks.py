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
def create_database(c, username="postgres", password="postgres", database_name="user_db"):
    c.run(f"docker run --name fastapi-sqlalchemy-db -e POSTGRES_PASSWORD={password} -e POSTGRES_DB={database_name} -p 5432:5432 -d {username}")

@task
def seed(c):
    c.run("PYTHONPATH=. python alembic/seed.py")

@task
def clear_data(c):
    c.run("PYTHONPATH=. python alembic/clear_data.py")
