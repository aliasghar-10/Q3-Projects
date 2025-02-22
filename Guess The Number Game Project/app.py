# Guess the Number Game in Python
import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!\n")
    print("The computer will pick a random number between 1 and 100. Can you guess it?\n")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get the user's guess
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please enter a number within the range of 1 to 100.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
