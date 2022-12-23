import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela = pygame.display.set_mode((1025, 700))
nome_do_jogo = pygame.display.set_caption('Brazar')

while True:
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()
