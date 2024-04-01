import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, punctuation=True):
    # Define character sets based on user preferences
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if punctuation:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage: generate a password of length 12 with all character sets enabled
password = generate_password()
print("Generated Password:", password)
