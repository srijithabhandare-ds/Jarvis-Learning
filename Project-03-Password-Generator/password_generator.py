# ============================
# Project 3 - Password Generator
# ============================

import random

# Character sets
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=<>?/"

print("=" * 35)
print("      PASSWORD GENERATOR")
print("=" * 35)

# Ask the user for password length
length = int(input("Enter password length: "))

# Ask whether to include numbers
include_numbers = input("Include numbers? (Y/N): ").strip().upper()

# Ask whether to include symbols
include_symbols = input("Include symbols? (Y/N): ").strip().upper()

# Base characters (always included)
characters = uppercase + lowercase

# Add numbers if user wants them
if include_numbers == "Y":
    characters += numbers

# Add symbols if user wants them
if include_symbols == "Y":
    characters += symbols

# Check if there are enough characters
if len(characters) == 0:
    print("Error: No characters available!")
else:

    # Build password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)

    # Password Strength
    if length < 8:
        strength = "Weak"
    elif length < 12:
        strength = "Medium"
    else:
        strength = "Strong"

    print(f"\nPassword Strength: {strength}")