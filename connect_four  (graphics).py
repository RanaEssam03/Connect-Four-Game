# Assignment 1 
# Rana Essam Ibrahim
# ID: 20210133
# Game_1: Connect_four with graphics (bonus task)

from turtle import color
import numpy as np
import pygame
import sys
from pygame.locals import *

def create_board(rows, cols):
    board = np.zeros((rows, cols))
    return board

def draw_board():
    for row in range(Rows):
        for col in range(Cols):
            pygame.draw.rect(screen, pink, (col*Square_size, row*Square_size+Square_size, Square_size, Square_size) )
            pygame.draw.circle(screen,black,  (col*Square_size + Square_size//2, row*Square_size+Square_size+Square_size//2), Radius)
    
    for row in range(Rows):
        for col in range(Cols):
            # TO update the board colors cope with players' inputs
            if board[row][col] == 1: # TO update the board colors cope with players' inputs
                pygame.draw.circle(screen,maroon,  (col*Square_size + Square_size//2, Hight -( row*Square_size+Square_size//2)), Radius)
            elif board[row][col] == 2:

                pygame.draw.circle(screen,blue,  (col*Square_size + Square_size//2, Hight -( row*Square_size+Square_size//2)), Radius)

def print_board(board):
    #to let the game start from down 
    board = np.flip(board, 0) 
    print(board)
    
# to update the game state
def drop_piece(board, row, col , piece):
    board [row][col] = piece


def is_valid_col(board, col):
    return board[5][col]==0


def get_empty_row(board, col):
    for row in range(Rows):
        if board[row][col] ==0:
            return row
            break
        

    
def is_win(piece):
    # check horizontal
    for row in range (Rows):
        for col in range(Cols-3):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
               return True
               
    # check vertical
    for row in range (Rows-3):
        for col in range(Cols):
            if board[row][col] == piece and board[row+3][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece:
                return True
                
    # check pos diagonal
    for row in range (Rows-3):
        for col in range(Cols-3):
            if board[row][col] == piece and board[row+3][col+3] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece:
                return True
                
    # check neg diagonal
    for row in range (3,Rows):
        for col in range(Cols-3):
            if board[row][col] == piece and board[row-3][col+3] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece:
                return True
def draw_game():
    for row in range(Rows):
        for col in range(Cols):
            if board[row] [col] == 0 :
                return False
    return True

# the used colors as (R,G,B)              
pink = (245,245,220)
black = (0, 0, 0)
blue = (25,25,112)
maroon = (128,0,0)
white = (255, 255, 255)


Rows = 6 
Cols = 7 

board = create_board(Rows, Cols) 


turn = 0 
game_over =  False

# the elements of the screen 
pygame.init() 
Square_size = 100
Radius = Square_size //2-5
Width = Cols * Square_size
Hight = (Rows+1) * Square_size
screen = pygame.display.set_mode((Width, Hight))
pygame.display.set_caption("connect Four")
icon = pygame.image.load("connect-four.png")
pygame.display.set_icon(icon)

game_font = pygame.font.SysFont("monospace", 75)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION: 
            x_pos = event.pos[0]
            if turn == 0:
                color = maroon
            else:
                color = blue  
            pygame.draw.rect(screen, black, (0,0, Width, Square_size)) 
            pygame.draw.circle(screen,color,  (x_pos, 45), Radius)  
        
        if draw_game() == True :
                pygame.draw.rect(screen, black, (0,0, Width, Square_size))
                # to create the statment
                Draw_text = game_font.render("Draw game :( !", True, white)
                # to indentify the statment's position on the screen
                Draw_rect = Draw_text.get_rect(center= (Width//2, Draw_text.get_height()//2))
                # to print the statment on the screen 
                screen.blit(Draw_text, Draw_rect)
                
                game_over= True # to end the game loop
                   
        if event.type == MOUSEBUTTONDOWN :
            x_pos = event.pos[0]
            col = x_pos//Square_size 
    
    
            if turn == 0:
                
                if is_valid_col(board, col):
                    row = get_empty_row(board, col)
                    drop_piece(board, row, col, 1)
                    if is_win(1):
                        pygame.draw.rect(screen, black, (0,0, Width, Square_size))
                        # to create the statment
                        won_text = game_font.render("Player 1 won !", True, maroon)
                        # to indentify the statment's position on the screen
                        won_rect = won_text.get_rect(center= (Width//2, won_text.get_height()//2))
                        # to print the statment on the screen 
                        screen.blit(won_text, won_rect)
                        
                        game_over= True # to end the game loop
                        
                    turn = 1
            else:
               
                if is_valid_col(board, col):
                    row = get_empty_row(board, col)
                    drop_piece(board, row, col, 2)
                    if is_win(2):
                        pygame.draw.rect(screen, black, (0,0, Width, Square_size))
                        # to create the statment
                        won_text = game_font.render("Player 2 won !", True, blue)
                        # to indentify the statment's position on the screen
                        won_rect = won_text.get_rect(center= (Width//2, won_text.get_height()//2))
                        # to print the statment on the screen 
                        screen.blit(won_text, won_rect)
                        
                        game_over= True #to end the game loop
                turn = 0
            
    draw_board()
    pygame.display.update()
    
    if game_over:
        #to close the screen
        pygame.time.delay(3000)
        
        