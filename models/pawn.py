'''This module define the pawns of the game'''
import pygame
from .constants import BLACK, WHITE, ROWS, SQUARE_SIZE


class Pawn:
    ''''''
    def __init__(self, row, col, color):
        ''''''
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.color = color
        self.king = False

        if self.color == BLACK:
            self.direction = -1
        else:
            self.directio = 1

    def position(self):
        '''Calculate position of a pawz based on its col and row'''
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.x = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def king(self):
        '''indicate if a pawn become a king '''
        self.king = True

    def draw_pawn(self, win):
         '''Function to draw a pawn
        Args:
            win (pygame.object): The window
        '''
        pygame.draw.circle(win, self.color, (self.x, self.y),
                           (SQUARE_SIZE//2 - 8))
        '''pygame.draw.circle(win, self.color, (self.x, self.y),
                           (SQUARE_SIZE//2 - 10))'''
