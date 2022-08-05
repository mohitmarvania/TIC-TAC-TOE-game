# This is the project to create a simple TIC-TAC-TOE game


import random


# Method to display the game board
def displayBoard(board):
    print("  |   |  ")
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("  |   |  ")
    print("---------")
    print("  |   |  ")
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("  |   |  ")
    print("---------")
    print("  |   |  ")
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("  |   |  ")


# Will take the choice from the player-1.
def User_input():
    select1 = ' '

    while select1 not in ['X', 'O']:
        select1 = input("Player - 1 will choose 'X' or 'O' : ")
        if select1.upper() == 'X':
            return ('X', 'O')
        elif select1.upper() == 'O':
            return ('O', 'X')


# Mark the 'X' or 'O' at the desired position
def Place_maker(board, position, marker):
    board[position] = marker


# Will check for the winning
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


# Will select random player to start the game
def choice_first():
    if random.randint(0, 1) == 1:
        return "Player - 1"
    else:
        return "Player - 2"


# Check if the position is empty or not
def Space_Check(board, position):
    return board[position] == ' '


# Take position from user
def User_Position(board, player):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or Space_Check(board, position) == False:
        position = int(input(f"{player} Choose your position from 1-9 : "))
    return position


# If the board is full.
def Final_board_check(board):
    for i in range(1, 10):
        if Space_Check(board, i):
            return False
    return True


# Method that ask if user want to play again
def Play_again():
    count = 0
    while count not in [1, 2]:
        answer = input("Do you want to play again ?? (Y or N) : ")
        if answer.upper() == 'Y':
            count = 1
            return True
        elif answer.upper() == 'N':
            count = 2
            return False


# The main part to call all the function to create the game

print("WELCOME TO THE TIC-TAC-TOE GAME")

while True:

    Board = [' '] * 10
    Player1_mark, Player2_mark = User_input()
    firstPlayer = choice_first()

    print(firstPlayer + " will go first.")
    confirm = input("Are you ready ?? (Y or N)")
    if confirm.upper() == 'Y':
        game_on = True
    elif confirm.upper() == 'N':
        game_on = False
    else:
        print("Sorry , I didn't get that.")
        print("Try Again !!")
        break

    while game_on:

        if firstPlayer == "Player - 1":
            displayBoard(Board)
            Position = User_Position(Board, "Player - 1 ")
            Place_maker(Board, Position, Player1_mark)

            if win_check(Board, Player1_mark):
                displayBoard(Board)
                print("Congratulations !! Player - 1 has won the game.")
                game_on = False
            else:
                if Final_board_check(Board):
                    displayBoard(Board)
                    print("The game is draw !!")
                    break
                else:
                    firstPlayer = "Player - 2"

        else:
            displayBoard(Board)
            Position = User_Position(Board, "Player - 2")
            Place_maker(Board, Position, Player2_mark)

            if win_check(Board, Player2_mark):
                displayBoard(Board)
                print("Congratulations !! Player - 2 has won the game.")
                game_on = False
            else:
                if Final_board_check(Board):
                    displayBoard(Board)
                    print("The game is draw !!")
                    break
                else:
                    firstPlayer = "Player - 1"

    if not Play_again():
        break
