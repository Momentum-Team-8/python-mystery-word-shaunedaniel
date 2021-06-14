from os import set_blocking
import random
import string

with open("words.txt") as words_txt:
    word_options = words_txt.read()
word = ["carrot", "bathroom"]
selection = list(len(word.upper) * "_")


def hangman():
    guess = input("Guess a letter: ").upper()

    while len()
