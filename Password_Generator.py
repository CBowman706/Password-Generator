Project Name: Random Password Generator
By: Cortney Bowman

This project involves basic string manipulation, user input, and randomness which are all essential programming concepts.


import random
import string

def generate_password(length=12):
    """Generate a secure random password with uppercase, lowercase, numbers, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Get user input for password length

try:
    length = int(input("Enter password length (minimum 8 characters): "))
    if length < 8:
        print("Password length too short, setting to 8 characters.")
        length = 8
except ValueError:
    print("Invalid input, setting default password length to 12.")
    length = 12



# Generate and display the password

secure_password = generate_password(length)
print(f"Your generated password: {secure_password}")





