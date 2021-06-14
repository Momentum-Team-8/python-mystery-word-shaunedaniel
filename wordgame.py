import random

print("Welcome to hangman!")


def get_word():
    words = ["cat", "dogs", "buttcrack"]
    return random.choice(words)


def game():
    word = get_word()
    word_list = []
    tries = 8
    print("This word has ", len(word), " letters.")
    yourmomma = (len(word) * "_ ")
    print(yourmomma)

    while tries > 0:
        correct_guesses = []
        incorrect_guesses = []
        letters_guessed = []
        guess = input("Your guess is ")
        if guess not in word:
            tries -= 1
            print("Sorry. Not a valid letter. You have " +
                  str(tries) + " tries")
        for x in word_list:
            if guess == x:
                letters_guessed.append(guess)
                correct_guesses.append(guess)
            elif x in correct_guesses:
                letters_guessed.append(x)
            else:
                letters_guessed.append("_")
                incorrect_guesses.append(guess)

            print(letters_guessed)


game()
