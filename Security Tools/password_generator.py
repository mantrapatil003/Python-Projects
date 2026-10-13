import random
import string

def generate_password(length=12):
    if length < 6:
        print("Password length should be at least 6 for security.")
        return None

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password_chars = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_chars = uppercase + lowercase + digits + special_chars
    password_chars += random.choices(all_chars, k=length - 4)

    random.shuffle(password_chars)

    password = ''.join(password_chars)
    return password

def main():
    print("Secure Password Generator")
    try:
        length = int(input("Enter desired password length (minimum 6): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    password = generate_password(length)
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
