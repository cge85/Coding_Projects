from random import randrange


def display_board(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] +   '   |   ' + board[0][1] +   '   |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1][0] +   '   |   ' + board[1][1] +   '   |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[2][0] +   '   |   ' + board[2][1] +   '   |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def enter_move(board):

    while True:
        move = int(input('Please pick a number within the range of squares (1-9):'))

        if move < 1 or move > 9:
            print('Please pick a number in the range of 1 through 9')
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print('Sorry that square already taken please use anothe square!')
            continue
        
        for row in range(0,3):
            for column in range(0,3):
                if board[row][column] == str(move):
                    board[row][column] = 'O'
        break

def make_list_of_free_fields(board):
    global free_square
    free_square = []
    for row in range(0,3):
        for colum in range(0,3):
            if board[row][colum] == 'X' or board[row][colum] == 'O':
                pass
            else:
                free_square.append(([row],[colum]))

def victory_for(board, sign):

    if sign == 'O':
        print('Checking to see if YOU are the winner!')
    else:
        print('Checking to see if the computer has won the game!')

    if board[0][0] == sign and board [0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board [1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board [2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board [1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board [1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board [1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board [1][1] == sign and board[2][2] == sign:
        return True
    elif board[2][0] == sign and board [1][1] == sign and board[0][2] == sign:
        return True
    else:
        print('We DO NOT have a winner yet!')


def draw_move(board):
    while True:
        row = randrange(3)
        column = randrange(3)

        if ([row], [column]) not in free_square:
            continue
        else:
            board[row][column] = 'X'
            return

board = [['1','2','3'], ['4', 'X','6'], ['7','8','9']]
numberOfMoves = 1
human = 'O'
computer = 'X'

print('Hallo and welcome to Tic-Tac-Toe!')
print('Here is the current status of out game board: ')
display_board(board)
print()

while  numberOfMoves < 9:
# This following code covers the user`s turn each round.
    enter_move(board)
    numberOfMoves += 1
    display_board(board)

    if victory_for(board, human) == True:
        print('You crushed the computer! You are a super human!')
        break
    else:
        print('Here si the current list of free squares')
        make_list_of_free_fields(board)
        print()
        display_board(board)

# This following code covers the computer`s turn each round.
    print()
    print('Now it is time for the computer to make its move!')
    draw_move(board)
    numberOfMoves += 1
    display_board(board)
    print()

    if victory_for(board, computer)  == True:
        print('The computer has outsmarted you once again, Human!!!')
        break
    else:
        print('Here si the current list of free squares')
        make_list_of_free_fields(board)
        print()
        display_board(board)
else:
    print('We have a tie!')

print('Thank you for playing, please play again soon!')