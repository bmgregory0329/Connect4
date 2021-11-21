import numpy as np
import sys

boardrows = 6
boardcols = 7

def create_board():
    board = np.zeros((boardrows,boardcols))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[boardrows-1][col] == 0

def get_next_open_row(board, col):
    for r in range(boardrows):
        if board[r][col] == 0:
            return r

def print_board(board, new=False):
    if doover == True:
        board = board[row][col] = 0
        return board
        print(board)
        doover == False
    else:
        print(np.flip(board, 0))

def play_again():
    restart = str(input("Would you like to play again (y/n)?"))
    if restart == "y":
        board = create_board()
        turn = 0
        doover = True
    else:
        game_over = False
        sys.exit()

def winning_move(board, piece):
    # Check horizontals
    for c in range(boardcols-3):
        for r in range(boardrows):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check verticals
    for c in range(boardcols):
        for r in range(boardrows-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check pos slope
    for c in range(boardcols-3):
        for r in range(boardrows-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check neg slope
    for c in range(boardcols-3):
        for r in range(3, boardrows):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

board = create_board()
game_over = False
turn = 0
doover = False

while not game_over:

    if doover == True:
        board = create_board()
        print_board(board, True)
        doover == False
    else:
        print_board(board)
        
    # Ask for Player 1 input
    if turn == 0:
        col = int(input("Player 1: Make your Selection (0-6): "))

        if is_valid_location(board,col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("PLAYER 1 WINS!")
                play_again()
            else:
                pass
                
        turn += 1

    #Ask for Player 2 input     
    else:
        col = int(input("Player 2: Make your Selection (0-6): "))

        if is_valid_location(board,col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("PLAYER 2 WINS!")
                play_again()
            else:
                pass

        turn -= 1
