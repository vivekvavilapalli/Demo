import re

def validate_phone(phone):
    pattern = r'^\+91\d{10}$'
    return re.match(pattern, phone)

def validate_email(email):
    pattern = r'^[\w\.-]+@(?:gmail\.com|org\.in|hotmail\.com)$'
    return re.match(pattern, email)

print("Hi, welcome to the phone book")

# Input phone number
while True:
    phone = input("1) Please enter your phone number: ")
    if validate_phone(phone):
        break
    else:
        print("Invalid phone number. Please enter a valid Indian phone number starting with +91 and 10 digits.")

# Input email
while True:
    email = input("2) Please enter your email: ")
    if validate_email(email):
        break
    else:
        print("Invalid email. Please enter a valid email (gmail.com, org.in, or hotmail.com).")

print(f"\nYour phone number is: {phone}")
print(f"Your email is: {email}")
print("complete")