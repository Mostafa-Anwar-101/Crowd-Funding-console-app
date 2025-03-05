import getpass
from utils import load_json, save_json, is_valid_email, is_valid_phone

USERS_FILE = "users.json"

def register():
    users = load_json(USERS_FILE)

    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    
    email = input("Enter your email: ").strip().lower()

    if not is_valid_email(email):
        print("Invalid email format.")
        return
    
    #check if email already registered
    for user in users:
        if user["email"] == email:
            print("Email already registered. Please log in.")
            return

    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    
    if password != confirm_password:
        print("Passwords do not match.")
        return

    phone = input("Enter your phone number: ").strip()
    if not is_valid_phone(phone):
        print("Invalid phone number.")
        return

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    }
    
    users.append(user)
    save_json(USERS_FILE, users)
    print("Registration successful! You can now log in.")

def login():
    users = load_json(USERS_FILE)

    email = input("Enter your email: ").strip().lower()
    password = getpass.getpass("Enter your password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Welcome back, {user['first_name']}!")
            return email

    print("Invalid email or password.")
    return None
