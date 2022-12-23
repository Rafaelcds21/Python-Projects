import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, '../conjunto imagens')
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'fantasy-tileset.png'))


class GoblinGuerreiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 18*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 40


class HumanoGuerreiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 18*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 40


class MeioOrcGuerreiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 18*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 40


class Elfoguerreiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 18*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 40


class Arqueiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 18*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 40


class Paladino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 18*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 40


class Mago(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 18*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 40


class Feiticeiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 18*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 40


lista_goblin_guerreiro = pygame.sprite.Group()
goblin_guerreiro = GoblinGuerreiro()
lista_goblin_guerreiro.add(goblin_guerreiro)

lista_humano_guerreiro = pygame.sprite.Group()
humano_guerreiro = HumanoGuerreiro()
lista_humano_guerreiro.add(humano_guerreiro)

lista_meio_orc_guerreiro = pygame.sprite.Group()
meio_orc_guerreiro = MeioOrcGuerreiro()
lista_meio_orc_guerreiro.add(meio_orc_guerreiro)

lista_elfo_guerreiro = pygame.sprite.Group()
elfo_guerreiro = Elfoguerreiro()
lista_elfo_guerreiro.add(elfo_guerreiro)

lista_arqueiro = pygame.sprite.Group()
arqueiro = Arqueiro()
lista_arqueiro.add(arqueiro)

lista_paladino = pygame.sprite.Group()
paladino = Paladino()
lista_paladino.add(paladino)

lista_mago = pygame.sprite.Group()
mago = Mago()
lista_mago.add(mago)

lista_feiticeiro = pygame.sprite.Group()
feiticeiro = Feiticeiro()
lista_feiticeiro.add(feiticeiro)

lista_player = pygame.sprite.Group()
lista_player.add(goblin_guerreiro)
lista_player.add(humano_guerreiro)
lista_player.add(meio_orc_guerreiro)
lista_player.add(elfo_guerreiro)
lista_player.add(arqueiro)
lista_player.add(paladino)
lista_player.add(mago)
lista_player.add(feiticeiro)
