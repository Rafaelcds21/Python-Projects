import pygame
from pygame.locals import *
from sys import exit

# escudo

pygame.init()

tela = pygame.display.set_mode((700, 700))

sprite_sheet = pygame.image.load('inimigo 1/sprite_0.png').convert_alpha()
sprite_sheet2 = pygame.image.load('escudo.png').convert_alpha()
velocidade = 2


class Escudo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_escudo = 25
        self.y_escudo = 550
        self.image = pygame.transform.scale(sprite_sheet2.subsurface((0, 0), (32, 32)), (32*3, 32*3))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.x_escudo
        self.rect.y = self.y_escudo


class Projetil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tx_projetil = 4
        self.ty_projetil = 4
        self.image = pygame.Surface([self.tx_projetil, self.ty_projetil])
        self.image.fill((255, 255, 255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 3


class Inimigo1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_inimigo1 = 50
        self.y_inimigo1 = 50
        self.image = pygame.transform.scale(sprite_sheet.subsurface((0, 0), (32, 32)), (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += velocidade


lista_projetil = pygame.sprite.Group()
projetil = Projetil()

nave = pygame.transform.scale(pygame.image.load('nave/sprite_0.png'), (32*3, 32*3))
x_nave = 300
y_nave = 600

grupo_escudo = pygame.sprite.Group()
escudo = Escudo()
grupo_escudo.add(escudo)

grupo_inimigo = pygame.sprite.Group()
inimigo1 = Inimigo1()
grupo_inimigo.add(inimigo1)

fps = pygame.time.Clock()

while True:
    fps.tick(30)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_w:
                y_nave = y_nave - 32

            if event.key == K_a:
                x_nave = x_nave - 32

            if event.key == K_s:
                y_nave = y_nave + 32

            if event.key == K_d:
                x_nave = x_nave + 32

            if event.key == K_1:

                projetil.rect.x = x_nave+48
                projetil.rect.y = y_nave+48

                lista_projetil.add(projetil)

    colisoes = pygame.sprite.spritecollide(projetil, grupo_inimigo, True, pygame.sprite.collide_mask)

    if colisoes:
        print('colidiu')

    tela.blit(nave, (x_nave, y_nave))

    lista_projetil.update()
    lista_projetil.draw(tela)

    grupo_inimigo.update()
    grupo_inimigo.draw(tela)

    grupo_escudo.update()
    grupo_escudo.draw(tela)

    pygame.display.flip()

