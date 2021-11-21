import numpy as np
import sys
import pygame
import math
import time
import tkinter as tk
from tkinter import messagebox
import os

_blue = (0,0,255)
_red = (255,0,0)
_yellow = (255,255,0)
_black = (0,0,0)

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

def print_board(board):
        print(np.flip(board, 0))

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

def draw_board(board):
    for c in range(boardcols):
        for r in range(boardrows):
            pygame.draw.rect(screen, _blue, (c*squaresz, r*squaresz+squaresz, squaresz, squaresz))
            pygame.draw.circle(screen, _black, (int(c*squaresz+squaresz/2), int(r*squaresz+squaresz+squaresz/2)), radius)
    for c in range(boardcols):
        for r in range(boardrows):
            if board[r][c] == 1:
                pygame.draw.circle(screen, _red, (int(c*squaresz+squaresz/2), height-int(r*squaresz+squaresz/2)), radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, _yellow, (int(c*squaresz+squaresz/2), height-int(r*squaresz+squaresz/2)), radius)
    pygame.display.update()
                
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost",True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def reset(board):
    python = sys.executable
    os.execl(python, python, * sys.argv)
    main()

def main():
    turn = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, _black, (0,0,width, squaresz))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, _red, (posx, int(squaresz/2)), radius)
                else:
                    pygame.draw.circle(screen, _yellow, (posx, int(squaresz/2)), radius)
            pygame.display.update()

            # Player 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, _black, (0,0,width, squaresz))
                #print(event.pos)
                if turn == 0:
                    posx = event.pos[0]
                    posy = event.pos[1]
                    
                    col = int(math.floor(posx/squaresz))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board,col)
                        drop_piece(board,row,col,1)

                        if winning_move(board, 1):
                            print("Player 1 Wins!")
                            message_box("Player 1 Wins!", "Congrats")
                            reset(board)
                        else:
                            print_board(board)
                            draw_board(board)

            # Player 2
                if turn == 1:
                    posx = event.pos[0]
                    posy = event.pos[1]
                    col = int(math.floor(posx/squaresz))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board,col)
                        drop_piece(board,row,col,2)

                        if winning_move(board, 2):
                            print("Player 2 Wins!")
                            message_box("Player 2 Wins!", "Congrats")
                            reset(board)
                        else:
                            print_board(board)
                            draw_board(board)

                turn +=1
                turn = turn % 2

game_over = False
pygame.init()
board = create_board()
squaresz = 100
width = boardcols * squaresz
height = (boardrows+1) * squaresz
size = (width,height)

radius = int(squaresz/2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
main()


main()




