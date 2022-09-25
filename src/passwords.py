import secrets
import string

# Reference: https://docs.python.org/3/library/secrets.html#recipes-and-best-practices

def generate_random_password(password_length):
    special_characters = "!@#$%^&*()"
    characters = string.ascii_letters + string.digits + special_characters
    attempts = 0
    while True:
        attempts += 1
        password = ''.join(secrets.choice(characters) for i in range(password_length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(check_characters(password, special_characters))):
            break
    print ("password generation attempts", str(attempts))
    return password

def check_characters(s, arr):
    return [characters in s for characters in arr]
    