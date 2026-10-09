from datetime import datetime
from .validation import validate_name, validate_age, validate_email

users = []

def add_user(name, age, email):
    if not validate_name(name):
        print("Ad duzgun deyil")
        return
    if not validate_age(age):
        print("Yas duzgun deyil")
        return
    if not validate_email(email):
        print("Email duzgun deyil")
        return
    user = {
        "name": name,
        "age": age,
        "email": email,
        "created_at": datetime.now().isoformat(timespec="seconds")
    }

    users.append(user)


def show_users():
    for user in users:
        print(
            f"{user['name']} - {user['age']} - {user['email']} - {user['created_at']}")


def is_adult(age):
    return age >= 18


if __name__ == "__main__":
    add_user("Test User", 18, "test@gmail.com")
    show_users()
