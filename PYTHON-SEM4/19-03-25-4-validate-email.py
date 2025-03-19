import re

def validate_email(email):
    pattern = r'^[a-z][a-z0-9]{7,}@[a-z]+\.[a-z]{2,3}$'
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("Enter your email: ")
if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
