import random
import string

def generate_password(length=12):
    if length < 6:
        print("⚠ Warning: It is recommended to use a length of at least 6 for security.")
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure at least one of each category
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password
    if length > 4:
        all_chars = lowercase + uppercase + digits + special_chars
        password_chars += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable pattern
    random.shuffle(password_chars)
    
    # Return as a string
    return ''.join(password_chars)

def main():
    print("🔐 Welcome to the Password Generator 🔐")
    
    try:
        length = int(input("Enter desired password length (Recommended: 12 or more): "))
        password = generate_password(length)
        print("\n✅ Your Generated Password:")
        print(password)
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
