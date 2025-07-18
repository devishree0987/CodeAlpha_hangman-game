import random

def hangman():
    """
    Implements a simple text-based Hangman game.
    """
    words = ["python", "intern", "coding", "alpha", "project"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("--- Welcome to Hangman! ---")
    print("Try to guess the word, one letter at a time.")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")
    print("-" * 30)

    while incorrect_guesses < max_incorrect_guesses:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")

        if display_word == secret_word:
            print(f"\n--- Congratulations! You guessed the word: '{secret_word}' ---")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    else: # This block executes if the while loop finishes without a 'break' (i.e., incorrect_guesses reached max)
        print("\n--- Game Over! You ran out of guesses. ---")
        print(f"The word was: '{secret_word}'")

if __name__ == "__main__":
    hangman()