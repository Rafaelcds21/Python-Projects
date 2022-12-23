import pygame
import os

pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, '../conjunto imagens')
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'fantasy-tileset.png'))


class Gosmasminions(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 21*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 128
class Gosmachefe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 21*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 128
class Escorpiao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 21*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 128
class LulaGigante(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 21*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 128
class Vampiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 21*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 128
class Mumia(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 21*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 128
class Bruxa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 21*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 128
class Beholder(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 21*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 128


class Goblin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 22*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 160
class Zumbi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 22*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 160
class Esqueleto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 22*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 160
class Orc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 22*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 160
class Barbaro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 22*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 160
        self.rect.topleft = (128, 160)
class Lobisomem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 22*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 160
        self.rect.topleft = (160, 160)
class Golem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 22*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 160
        self.rect.topleft = (192, 160)
class Darklord(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 22*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 160
        self.rect.topleft = (224, 160)


lista_inimigos = pygame.sprite.Group()
lista_gosmas_minions = pygame.sprite.Group()
gosmas_minions = Gosmasminions()
gosmachefe = Gosmachefe()
escorpiao = Escorpiao()
lula_gigante = LulaGigante()
vampiro = Vampiro()
mumia = Mumia()
bruxa = Bruxa()
beholder = Beholder()
goblin = Goblin()
zumbi = Zumbi()
esqueleto = Esqueleto()
orc = Orc()
barbaro = Barbaro()
lobisomem = Lobisomem()
golem = Golem()
darklord = Darklord()
lista_gosmas_minions.add(gosmas_minions)
lista_inimigos.add(gosmas_minions)
lista_inimigos.add(gosmachefe)
lista_inimigos.add(escorpiao)
lista_inimigos.add(lula_gigante)
lista_inimigos.add(vampiro)
lista_inimigos.add(mumia)
lista_inimigos.add(bruxa)
lista_inimigos.add(beholder)
lista_inimigos.add(goblin)
lista_inimigos.add(zumbi)
lista_inimigos.add(esqueleto)
lista_inimigos.add(orc)
lista_inimigos.add(barbaro)
lista_inimigos.add(lobisomem)
lista_inimigos.add(golem)
lista_inimigos.add(darklord)
