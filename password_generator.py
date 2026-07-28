import random
import string


def generate_password(length, use_symbols):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    characters = letters + numbers

    if use_symbols:
        characters += symbols

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("=" * 40)
print("      Python Password Generator")
print("=" * 40)

while True:
    try:
        length = int(input("Enter password length: "))

        if length < 8:
            print("Password should be at least 8 characters.\n")
            continue

        break

    except ValueError:
        print("Please enter a valid number.\n")

choice = input("Include special characters? (y/n): ").lower()

if choice == "y":
    use_symbols = True
else:
    use_symbols = False

password = generate_password(length, use_symbols)

print("\nYour secure password is:\n")
print(password)

print("\nPassword generated successfully!")