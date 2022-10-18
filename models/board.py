'''This module define the boad of the game'''
import pygame
from .constants import BLACK, WHITE, ROWS, SQUARE_SIZE


class Board:
    '''Class Board to draw the checker board surface'''
    def __init__(self):
        '''initialisation of an  board'''
        self.board = []
        self.selected_piece = None

    def draw_cases(self, win):
        '''Draws all square of of the checker
        Args:
            win (pygame.display): the surface where we draw
        '''
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE,
                                              col * SQUARE_SIZE, SQUARE_SIZE,
                                              SQUARE_SIZE))

    def fill_board(self):
         
