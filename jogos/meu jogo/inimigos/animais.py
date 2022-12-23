import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, '../conjunto imagens')
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'fantasy-tileset.png'))


class Rato(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 19*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 100)


class AranhaMinion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 19*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 100)


class Lagarto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 19*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 100)


class AranhaChefe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 19*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 100)


class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 19*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 100)


class Besouro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 19*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 100)


class Lacraia(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 19*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 100)


class Onix(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 19*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 100)


class Arvore(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 20*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 200)


class Coelho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 20*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 200)


class Morcego1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 20*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 200)


class Morcego2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 20*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 200)


class Cobra(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 20*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 200)


class Lobo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 20*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 200)


class Javali(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 20*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 200)


class Urso(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 20*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 200)


lista_animais = pygame.sprite.Group()
rato = Rato()
aranha_minion = AranhaMinion()
lagarto = Lagarto()
aranha_chefe = AranhaChefe()
sapo = Sapo()
besouro = Besouro()
lacraia = Lacraia()
onix = Onix()
arvore = Arvore()
coelho = Coelho()
morcego1 = Morcego1()
morcego2 = Morcego2()
cobra = Cobra()
lobo = Lobo()
javali = Javali()
urso = Urso()
lista_animais.add(rato)
lista_animais.add(aranha_minion)
lista_animais.add(lagarto)
lista_animais.add(aranha_chefe)
lista_animais.add(sapo)
lista_animais.add(besouro)
lista_animais.add(lacraia)
lista_animais.add(onix)
lista_animais.add(arvore)
lista_animais.add(coelho)
lista_animais.add(morcego1)
lista_animais.add(morcego2)
lista_animais.add(cobra)
lista_animais.add(lobo)
lista_animais.add(javali)
lista_animais.add(urso)

tela = pygame.display.set_mode((256, 256))
nome = pygame.display.set_caption('animais')

while True:
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    lista_animais.draw(tela)
    lista_animais.update()

    pygame.display.update()
