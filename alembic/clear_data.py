from app.models import User
from app.database import SessionLocal

db = SessionLocal()


def delete_all_users():
    db.query(User).delete()
    db.commit()
    print("All users have been removed.")


def main():
    # Call delete functions for each type of data
    delete_all_users()
    print("\n---------------------------")
    print("All data have been removed.")

if __name__ == "__main__":
    main()
