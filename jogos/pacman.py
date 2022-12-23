import pygame
from pygame.locals import *
from sys import *

pygame.init()

tela = pygame.display.set_mode((1025, 700))
nome = pygame.display.set_caption('Pacman')

sprite_sheet = pygame.image.load('pacman e fantasmas.png').convert_alpha()
# sprite_sheet_grid = pygame.image.load().convert_alpha()


class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.lista_imagens = []

        for i in range(0, 3):
            img = pygame.transform.scale(sprite_sheet.subsurface((0, 0), (32, 32)), (32*3, 32*3))
            self.lista_imagens.append(img)

        self.index_lista = 0
        self.image = self.lista_imagens[self.index_lista]

        self.x_pacman = 200
        self.y_pacman = 100

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = self.x_pacman
        self.rect.y = self.y_pacman

    def update(self):
        if self.index_lista >= 2:
            self.index_lista = 0

        self.index_lista += 0.25
        self.image = self.lista_imagens[int(self.index_lista)]


class Fantasmas(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(sprite_sheet.subsurface((64, 0), (32, 32)), (32*3, 32*3))

        self.x_fantasma = 100
        self.y_fantasma = 100

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = self.x_fantasma
        self.rect.y = self.y_fantasma


# class Grid(pygame.sprite.Sprite):
    # def __init__(self):
        # super().__init__()
        # self.image = pygame.transform.scale(sprite_sheet_grid.subsurface((0, 0), (32, 32)), (32 * 3, 32 * 3))
        # self.rect = self.image.get_rect()
        # self.mask = pygame.mask.from_surface(self.image)


pacman = Pacman()
fantasmas = Fantasmas()
# grid = Grid()

lista_total = pygame.sprite.Group()
lista_total.add(pacman)
lista_total.add(fantasmas)

while True:
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_w:
                pacman.rect.y -= 2
            if event.key == K_s:
                pacman.rect.y += 2
            if event.key == K_a:
                pacman.rect.x -= 2
            if event.key == K_d:
                pacman.rect.x += 2

    lista_total.update()
    lista_total.draw(tela)

    pygame.display.flip()
