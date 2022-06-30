import random

# game rules! Rock wins against scissors, Scissors wins againt paper, Paper wins against rock
def game():
    user = input("What`s your choice ? 'r' for rock, 'p' for paper, 's' for scissors: \n")
    computer = random.choice(['r', 'p', 's'])

    while user != 'r' and 'p' and 's':
        print('Please enter one of the letters of the game to play!')
        return game()

    if user == computer:
        return 'I\'ts a tie!'

    if is_winner(user, computer):
        return 'You won!'

    return 'You lost!'


def is_winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(game())
