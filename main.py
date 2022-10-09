'''The main file'''
import pygame
from models.constants import WIDTH, HEIGHT
from models.board import Board


pygame.init()

pygame.display.set_caption("checkerboard")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

    running = True
    clock = pygame.time.Clock()
    board = Board()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_cases(WIN)
        pygame.display.update()

    pygame.quit()

main()
