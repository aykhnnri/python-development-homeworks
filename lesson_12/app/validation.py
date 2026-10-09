def validate_name(name):
    return len(name.strip()) >= 2

def validate_age(age):
    return age >= 0

def validate_email(email):
    return "@" in email and "." in email