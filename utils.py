import json
import re
import os

def load_json(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
            return json.load(file)
        

def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def is_valid_phone(phone):
    pattern = r"^(010|011|012|015)[0-9]{8}$"
    return re.match(pattern, phone)
