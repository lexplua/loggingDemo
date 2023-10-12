import random


def game_loop():
    scores = dict(
        computer_score=0,
        player_score=0
    )

    current_guessed_number = guess_number()
    player_number = read_player_number()
    win = compare_input(current_guessed_number, player_number)
    update_print_scores(scores, win)

    while player_number != 0:
        guess_number()
        player_number = read_player_number()
        win = compare_input(current_guessed_number, player_number)
        update_print_scores(scores, win)


def guess_number():
    guessed = random.randint(1, 10)
    return guessed


def read_player_number():
    player_number = input("Enter your guess or 0 to end the game:")
    return int(player_number)


def compare_input(guessed_number, player_number):
    try:
        if guessed_number == player_number:
            print("WOW 😯 you won !")
            return True
        else:
            print(f"You looose 😜!")
            return False
    finally:
        print('*' * 20)


def update_print_scores(scores, win):
    if win:
        scores['player_score'] += 1
    else:
        scores['computer_score'] += 1
    print(f"Current score\n🤖: {scores['computer_score']} 👩‍💻: {scores['player_score']}")


game_loop()
