#Strong Password Generator
password_length = int(input("Enter the desired password length: "))
# Define the character sets to use in the password
import random
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "!@#$%^&*()-+"

all_characters = lowercase_letters + uppercase_letters + digits + special_characters
password = ""
print("Generating a strong password...")
# Ensure the password contains at least one character from each set
password += random.choice(lowercase_letters)
password += random.choice(uppercase_letters)
password += random.choice(digits)
password += random.choice(special_characters)

# Fill the rest of the password with random characters from all sets
for _ in range(password_length - 4):
    password += random.choice(all_characters)

print(f"Generated strong password: {password}")