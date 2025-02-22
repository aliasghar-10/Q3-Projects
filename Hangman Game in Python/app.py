# Hangman Game in Python
import random

def hangman():
    print("Welcome to the Hangman Game!\n")

    # List of words for the game
    word_list = ["python", "hangman", "developer", "programming", "computer", "algorithm", "function"]
    chosen_word = random.choice(word_list)
    guessed_word = ["_" for _ in chosen_word]
    attempts = 6
    guessed_letters = []

    print("Let's start! You have 6 attempts to guess the word.")

    while attempts > 0:
        print("\nWord: " + " ".join(guessed_word))
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Get user's guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter! Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print(f"Good job! {guess} is in the word.")
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! {guess} is not in the word.")
            attempts -= 1

        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word: " + chosen_word)
            break

    if "_" in guessed_word:
        print("\nSorry, you've run out of attempts. The word was: " + chosen_word)

# Run the game
if __name__ == "__main__":
    hangman()
