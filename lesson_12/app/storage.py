from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORT_FILE = DATA_DIR / "users_report.txt"
USER_FILE = DATA_DIR / "users.json"

def export_user(user_list):
    DATA_DIR.mkdir(exist_ok=True)

    with open(REPORT_FILE, "a", encoding="utf-8") as file:
        file.write("--- User siyahisi ---\n")

        for user in user_list:
            file.write(
                f"{user['name']} | "
                f"{user['age']} | "
                f"{user['email']} | "
                f"{user['created_at']}\n"
            )

def save_user(user_list):
    DATA_DIR.mkdir(exist_ok=True)

    with open(USER_FILE, "w", encoding="utf-8") as file:
        json.dump(
            user_list,
            file,
            ensure_ascii=False,
            indent=4
        )

def load_users():
    if not USER_FILE.exists():
        return []

    with open(USER_FILE, "r", encoding="utf-8") as file:
        return json.load(file)