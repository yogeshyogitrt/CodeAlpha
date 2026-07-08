import random

def play_hangman():
    word_list = ["python", "syntax", "variable", "boolean", "function"]
    secret_word = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6
    print("Welcome to Text-Based Hangman!")
    print(f"You have {max_guesses} incorrect guesses allowed.")
    while incorrect_guesses < max_guesses:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                
        print(f"\nWord to guess: {display_word}")
        print(f"Incorrect guesses left: {max_guesses - incorrect_guesses}")
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: '{secret_word}'.")
            return  
        guess = input("Guess a single letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter exactly one letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1
    print(f"\nGame Over! You ran out of guesses. The correct word was '{secret_word}'.")
if __name__ == "__main__":
    play_hangman()
