import json

user = {
    "name": "Ayxan",
    "age": 24,
    "email": "aykhan@gmail.com"
}

json_text = json.dumps(user, ensure_ascii=False, indent=4)

print(json_text)
print(type(json_text))

restored_user = json.loads(json_text)

print(restored_user)
print(type(restored_user))
print(type(restored_user["age"]))