# Password Generator in Python
import random
import string

def generate_password():
    print("Welcome to the Password Generator!\n")

    try:
        # Get the desired length of the password from the user
        length = int(input("Enter the desired password length (minimum 6): "))
        if length < 6:
            print("Password length must be at least 6 characters.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Character pools for the password
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password contains at least one character from each category
    all_chars = lower_case + upper_case + digits + special_chars
    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password to make it random
    random.shuffle(password)

    # Join the list to form the final password
    final_password = ''.join(password)

    print(f"\nYour generated password is: {final_password}\n")

# Run the password generator
if __name__ == "__main__":
    generate_password()
