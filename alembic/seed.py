from sqlalchemy.exc import IntegrityError
from app.models import User
from app.database import SessionLocal

db = SessionLocal()


def create_user(user_data):
    name = user_data["name"]
    existing_user = db.query(User).filter(User.name == user_data["name"]).first()
    if existing_user:
        print(f"User with name '{name}' already exists. Skipping.")
        return existing_user

    try:
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        print(f"User with name '{name}' created.")
        return user
    except IntegrityError as e:
        db.rollback()
        print(f"Error creating user with name '{name}': {e}")


def seed_users():
    users_data = [
        {"name": "John Doe"},
        {"name": "Jane Doe"},
        {"name": "Alice"},
        {"name": "Bob"},
    ]
    for user_data in users_data:
        create_user(user_data)


def main():
    # Call seed functions for each type of data
    seed_users()


if __name__ == "__main__":
    main()
