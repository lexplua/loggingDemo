import random
# TODO: Exercise
# 1. Play the game
# 2. Do logging exercises, marked with TODO: TASK
# 3. Look at the logs and find error in program

# TODO: TASK 1 add import to use logging module
# import ...

# TODO: TASK 2 create logging config
# logging.basicConfig(
#     level= ... ,
#     filename="game.log"
# )

# For every new file - new logger
# TODO: TASK 3 create logger
# LOGGER = ...


def guess_number():
    guessed = random.randint(1, 10)
    return guessed


def read_player_number():
    player_number = input("Enter your guess or 0 to end the game:")
    return int(player_number)


def compare_input(guessed_number, player_number):
    try:
        if guessed_number == player_number:
            print("\tWOW 😯 you won !")
            return True
        else:
            print(f"\tYou looose 😜!")
            return False
    finally:
        print(f"\t{'*' * 20}")
        print()


def update_print_scores(scores, win):
    if win:
        scores['player_score'] += 1
    else:
        scores['computer_score'] += 1
    print(f"\tCurrent score\n\t🤖: {scores['computer_score']} 👩‍💻: {scores['player_score']}")


def game_loop():
    scores = dict(
        computer_score=0,
        player_score=0
    )

    # TODO: TASK 4 add scores logging
    # LOGGER.debug(f"Scores {...}")

    # TODO: TASK 5 add scores logging
    current_guessed_number = guess_number()
    # LOGGER.debug(f"Guessed number {...}")

    # TODO: TASK 6 add player number logging
    player_number = read_player_number()
    # LOGGER.info(...)

    win = compare_input(current_guessed_number, player_number)

    update_print_scores(scores, win)
    # TODO: TASK 7 add logging for updated(new) scores
    # ...

    while player_number != 0:
        guess_number()
        player_number = read_player_number()
        win = compare_input(current_guessed_number, player_number)
        update_print_scores(scores, win)

    # Game is over
    # TODO: TASK 8 Add Final results logging
    # ...


if __name__ == "__main__":
    game_loop()
