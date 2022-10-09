'''The main file'''
import pygame
from models.constants import WIDTH, HEIGHT

pygame.init()



pygame.display.set_caption("checkerboard")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()

main()
