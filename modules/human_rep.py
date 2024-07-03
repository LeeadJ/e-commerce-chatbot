import re
import csv

def is_valid_name(name):
    return bool(re.match(r"^[A-Za-z]+(?: [A-Za-z]+)+$", name))

def is_valid_email(email):
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))

def is_valid_phone(phone):
    return bool(re.match(r"^\+?[0-9]\d{1,14}$", phone))

def request_human_representative_info():
    while True:
        name = input("Please provide your full name: ")
        while not is_valid_name(name) or name == "exit":
            if name.lower() == "exit":
                return None, None, None
            print("Invalid name. Enter a valid full name using only letters and spaces or type 'exit'.")
            name = input("Please enter your full name: ")

        email = input("Please provide your email: ")
        while not is_valid_email(email) or email == "exit":
            if email.lower() == "exit":
                return None, None, None
            print("Invalid email. Enter a valid email address or type 'exit'.")
            email = input("Please enter your email: ")

        phone = input("Please provide your phone number: ")
        while not is_valid_phone(phone) or phone == "exit":
            if phone.lower() == "exit":
                return None, None, None
            print("Invalid phone. Enter a valid phone number or type 'exit'.")
            phone = input("Please enter your phone number: ")

        return name, email, phone

def isHumanRepresentativeRequest(user_input):
    phrases = [
        'human representative', 'talk to a person', 'speak to a person', 'talk to a human', 'speak to a human',
        'contact human', 'contact representative', 'need help from a person', 'need to talk to someone',
        'connect me with a human', 'connect with a representative', 'human assistance', 'real person',
        'live agent', 'customer service', 'customer support', 'talk someone', 'talk human', 'speak human',
        'talk person', 'speak person', 'contact person', 'human rep', 'want rep', 'need rep', 'speak representative'
    ]
    for phrase in phrases:
        words = phrase.split()
        if all(word in user_input for word in words):
            return True
    return False

def save_contact_info(name, email, phone):
    with open('data/contact_info.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])
    return "Your contact information has been saved. A representative will contact you shortly."
