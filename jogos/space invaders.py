import pygame
from pygame.locals import *
from sys import exit

# Problemas: Multiplicar os inimigos, impedir os tiros de atravessarem o escudo e multiplica-los, criar os segundos inimigos

pygame.init()

tela = pygame.display.set_mode((1024, 700))
nome_do_jogo = pygame.display.set_caption('Space Invaders')

sprite_sheet = pygame.image.load('inimigo 1/sprite_0.png').convert_alpha()
sprite_sheet2 = pygame.image.load('escudo.png').convert_alpha()
velocidade = 1


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.nave = pygame.image.load('nave/sprite_0.png')
        self.image = pygame.transform.scale(self.nave, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.x_nave = 400
        self.y_nave = 600
        self.rect.x = self.x_nave
        self.rect.y = self.y_nave


class Escudo1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_escudo1 = 35
        self.y_escudo1 = 475
        self.image = pygame.transform.scale(sprite_sheet2.subsurface((0, 0), (32, 32)), (32*4, 32*5))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.x_escudo1
        self.rect.y = self.y_escudo1


class Escudo2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_escudo2 = 291
        self.y_escudo2 = 475
        self.image = pygame.transform.scale(sprite_sheet2.subsurface((0, 0), (32, 32)), (32*4, 32*5))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.x_escudo2
        self.rect.y = self.y_escudo2


class Escudo3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_escudo3 = 547
        self.y_escudo3 = 475
        self.image = pygame.transform.scale(sprite_sheet2.subsurface((0, 0), (32, 32)), (32*4, 32*5))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.x_escudo3
        self.rect.y = self.y_escudo3


class Escudo4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_escudo4 = 803
        self.y_escudo4 = 475
        self.image = pygame.transform.scale(sprite_sheet2.subsurface((0, 0), (32, 32)), (32*4, 32*5))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.x_escudo4
        self.rect.y = self.y_escudo4


class Projetil(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 4])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y -= 3


class Inimigo1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_inimigo1 = 50
        self.y_inimigo1 = 50
        self.image = pygame.transform.scale(sprite_sheet.subsurface((0, 0), (32, 32)), (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_inimigo1
        self.rect.y = self.y_inimigo1
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += velocidade


class Projetil_inimigo1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 4])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += 3


contador = 0

nave = Nave()
projetil = Projetil()
inimigo1 = Inimigo1()
escudo1 = Escudo1()
escudo2 = Escudo2()
escudo3 = Escudo3()
escudo4 = Escudo4()
projetil_inimigo1 = Projetil_inimigo1()

lista_total = pygame.sprite.Group()
lista_total.add(nave)
lista_total.add(inimigo1)
lista_total.add(escudo1)
lista_total.add(escudo2)
lista_total.add(escudo3)
lista_total.add(escudo4)

lista_projetil = pygame.sprite.Group()

grupo_inimigo1 = pygame.sprite.Group()
grupo_inimigo1.add(inimigo1)
grupo_inimigo1.add(projetil_inimigo1)

fps = pygame.time.Clock()

while True:
    fps.tick(30)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        elif event.type == KEYDOWN:
            if event.key == K_w:
                nave.rect.y = nave.rect.y - 32

            if event.key == K_a:
                nave.rect.x = nave.rect.x - 32

            if event.key == K_s:
                nave.rect.y = nave.rect.y + 32

            if event.key == K_d:
                nave.rect.x = nave.rect.x + 32

            if event.key == K_1:
                projetil.rect.x = nave.rect.x+48
                projetil.rect.y = nave.rect.y+48

                lista_total.add(projetil)
                lista_projetil.add(projetil)

    colisoes = pygame.sprite.spritecollide(projetil, grupo_inimigo1, True, pygame.sprite.collide_mask)

    if colisoes:
        print('colidiu')

    lista_total.update()
    lista_total.draw(tela)

    pygame.display.flip()
