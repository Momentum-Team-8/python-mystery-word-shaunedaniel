import random

with open("words.txt", 'r') as w:
    allText = w.read()


def gamePrompt():
    words = list(map(str, allText.split()))
    word = (random.choice(words))
    # for letter of words:
    wordLetters = list(word)
    wordLength = (len(wordLetters))
    print(wordLength)

    # if letters ==

    # input("Your guess: ")
    # word_selection = "_" * len(words)


gamePrompt()
