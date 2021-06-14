def mystery_word_game():
    attempts = 8
    test = wordChoice
    word_list = []

    # word_guess = ""
    for x in test:
        word_list.append(x)
    print(test)

    correct_guesses = []
    incorrect_guesses = []
    while tries < 8:
        current_progress = []
        player_guess = input("What letter do you guess? ")
        if len(player_guess) > 1:
            print("Your guess must be one letter!")
            player_guess = input("What letter do you guess? ")
        if player_guess not in word_list:
            tries += 1
        if player_guess in correct_guesses:
            print("You already guessed that, try again!")
        for x in word_list:
            if player_guess == x:
                current_progress.append(player_guess)
                correct_guesses.append(player_guess)
            elif x in correct_guesses:
                current_progress.append(x)
            else:
                current_progress.append("_")
                incorrect_guesses.append(player_guess)
        while attempts == 8:
            print("You lose! Your word was: " + test)
            break
        print("".join(current_progress))
