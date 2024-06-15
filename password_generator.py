# password_generator.py

import string
import random

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define the characters to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one lowercase letter, one uppercase letter, one digit, and one special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length-4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        if length < 4:
            print("Password length should be at least 4 characters.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")

        next_action = input("Do you want to generate another password? (yes/no): ")
        if next_action.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
