import random
import string

def display_intro():
    print("\n========== PASSWORD GENERATOR ==========")
    print("Create a strong and secure password as per your preferences.\n")

def get_user_input():
    """
    Ask the user to input password preferences:
    length, use of uppercase, numbers, and symbols.
    """
    try:
        length = int(input("Enter password length (minimum 6): "))
        if length < 6:
            print("Password length too short! Try again.\n")
            return get_user_input()

        use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
        use_digits = input("Include NUMBERS? (y/n): ").lower() == 'y'
        use_symbols = input("Include SYMBOLS? (y/n): ").lower() == 'y'

        return length, use_upper, use_digits, use_symbols

    except ValueError:
        print("Invalid input! Please enter a number for length.\n")
        return get_user_input()

def generate_password(length, upper, digits, symbols):
    """
    Generate a password based on user choices.
    """
    characters = list(string.ascii_lowercase)

    if upper:
        characters += list(string.ascii_uppercase)
    if digits:
        characters += list(string.digits)
    if symbols:
        characters += list("!@#$%^&*()-_=+[]{}|;:,.<>?/")

    if not characters:
        return "Error: No character types selected!"

    # Generate a secure password using random.choices
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    display_intro()
    length, use_upper, use_digits, use_symbols = get_user_input()
    password = generate_password(length, use_upper, use_digits, use_symbols)

    print("\n🔐 Your generated password is:\n" + password)
    print("✅ Password successfully generated and ready to use!")
    print("\nKeep it safe and do not share it with anyone!\n")

if __name__ == "__main__":
    main()
