import app.users as users_service
from app.storage import export_user, load_users, save_user

loaded_users = load_users()

users_service.users.clear()
users_service.users.extend(loaded_users)

print("Fayldan oxunan user sayi:", len(users_service.users))

print("--- Fayldan berpa olunan userler ---")
users_service.show_users()

users_service.add_user("Fuad", 27, "fuad@gmail.com")
users_service.add_user("Nicat", 22, "nicat@gmail.com")

save_user(users_service.users)
export_user(users_service.users)

print("--- Cari userler ---")
users_service.show_users()

print("Umumi user sayi:", len(users_service.users))