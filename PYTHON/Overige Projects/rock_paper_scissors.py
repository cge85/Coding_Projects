import random


def play():
    user = input(
        "What is your choice ? 'r' for rock, 'p' for paper, 's' for scissors: \n")
    computer = random.choice(['r', 'p', 's'])

    while user != 'r' and 'p' and 's':
        print('Please input the correct letter of the game!')
        return play()

    if user == computer:
        return 'it\'s a tie.'

    # r > s, s > p, p > r
    if is_winner(user, computer):
        return 'You won!'
    return 'you lose!'


def is_winner(player, opponent):
    # return true if the player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
