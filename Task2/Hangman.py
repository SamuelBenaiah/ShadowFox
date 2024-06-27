import random

def print_hangman(attempts):
    stages = [
        '''
           -----
           |   |
               |
               |
               |
               |
        =========''', '''
           -----
           |   |
           O   |
               |
               |
               |
        =========''', '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========''', '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========''', '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========''', '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========''', '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========='''
    ]
    print(stages[6 - attempts])

def hangman():
    words = {
        'python': 'a programming language',
        'kotlin': 'a programming language',
        'banana': 'a fruit',
        'rocket': 'a space vehicle',
        'monkey': 'an animal'
    }
    word, hint = random.choice(list(words.items()))
    guessed_letters = set()
    correct_letters = set(word)
    attempts = 6
    display_word = ['_'] * len(word)

    print("Welcome to Hangman!")
    print(f"Hint: {hint}")

    while attempts > 0:
        print("\n" + " ".join(display_word))
        print_hangman(attempts)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in correct_letters:
            guessed_letters.add(guess)
            for idx, letter in enumerate(word):
                if letter == guess:
                    display_word[idx] = guess
            if '_' not in display_word:
                print("\n" + " ".join(display_word))
                print("Congratulations, you won!")
                break
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts remaining.")

        if attempts == 0:
            print("\n" + " ".join(display_word))
            print_hangman(attempts)
            print(f"Sorry, you lost. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
