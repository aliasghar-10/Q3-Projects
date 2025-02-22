# Guess the Number Game (User Picks) in Python
import random

def computer_guesses_number():
    print("Welcome to the Guess the Number Game: Computer Edition!\n")
    print("Think of a number between 1 and 100, and I will try to guess it.\n")

    low = 1
    high = 100
    attempts = 0

    input("Press Enter when you're ready with your number...")

    while low <= high:
        attempts += 1
        guess = random.randint(low, high)
        print(f"I guess: {guess}")
        
        feedback = input("Is it correct (c), too high (h), or too low (l)? ").lower()

        if feedback == "c":
            print(f"Hooray! I guessed your number {guess} correctly in {attempts} attempts!")
            break
        elif feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        else:
            print("Invalid input! Please enter 'c' for correct, 'h' for too high, or 'l' for too low.")

    if low > high:
        print("Hmm, something went wrong. Did you give me the right feedback?")

# Run the game
if __name__ == "__main__":
    computer_guesses_number()

