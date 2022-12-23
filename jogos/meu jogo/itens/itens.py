import pygame
import os

pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, '../conjunto imagens')
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'fantasy-tileset.png'))


class BauFechado(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 4*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
class BauAberto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 4*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 0
class Chave1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 4*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 0
class Chave2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 4*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 0
class Chave3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 4*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 0
class Chave4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 4*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 0
class Chave5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 4*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 0
class Chave6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 4*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 0


class Pocao1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 5*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 32
class Pocao2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 5*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 32
class Pocao3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 5*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 32
class Pocao4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 5*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 32
class Pocao5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 5*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 32
class Pocao6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 5*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 32
class Pocao7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 5*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 32
class Pocao8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 5*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 32


class Papeis(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 6*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 64
class Pergaminho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 6*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 64
class RoloPergaminho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 6*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 64
class Mapa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 6*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 64
class LivroAberto1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 6*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 64
class LivroAberto2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 6*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 64
class LivroFechado1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 6*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 64
class LivroFechado2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 6*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 64


class Espada1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 7*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 96
class Espada2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 7*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 96
class Espada3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 7*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 96
class Espada4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 7*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 96
class Espada5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 7*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 96
class Espada6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 7*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 96
class Espada7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 7*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 96
class Espada8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 7*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 96


class Machado1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 8*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 128
class Machado2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 8*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 128
class Machado3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 8*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 128
class Machado4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 8*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 128
class Machado5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 8*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 128
class Machado6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 8*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 128
class Machado7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 8*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 128
class Machado8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 8*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 128


class Shuriken1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 9*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 160
class Shuriken2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 9*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 160
class Espadas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 9*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 160
class Arco1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 9*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 160
class Arco2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 9*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 160
class Arco3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 9*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 160
class Crossbow1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 9*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 160
class Crossbow2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 9*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 160


class MiniBomba(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 10*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 192
class BombaMedia(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 10*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 192
class BombaGrande(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 10*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 192
class Miniflecha(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 10*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 192
class FlechaMedia(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 10*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 192
class FlechaGrande(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 10*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 192
class Dardos1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 10*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 192
class Dardos2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 10*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 192


class Armadura1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 11*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 224
class Armadura2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 11*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 224
class Armadura3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 11*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 224
class Armadura4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 11*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 224
class Armadura5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 11*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 224
class Armadura6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 11*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 224
class Armadura7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 11*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 224
class Armadura8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 11*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 224


class Capacete1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 12*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 256
class Capacete2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 12*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 256
class Capacete3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 12*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 256
class Capacete4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 12*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 256
class Capacete5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 12*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 256
class Capacete6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 12*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 256
class Capacete7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 12*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 256
class Capacete8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 12*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 256


class Escudo1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 13*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 288
class Escudo2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 13*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 288
class Escudo3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 13*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 288
class Escudo4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 13*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 288
class Escudo5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 13*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 288
class Escudo6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 13*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 288
class Escudo7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 13*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 288
class Escudo8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 13*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 288


class Cajado1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 14*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 320
class Cajado2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 14*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 320
class Cajado3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 14*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 320
class Cajado4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 14*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 320
class Cajado5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 14*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 320
class Cajado6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 14*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 320
class Cajado7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 14*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 320
class Cajado8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 14*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 320


class PoucasMoedas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0*32, 15*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 352
class MuitasMoedas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1*32, 15*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 352
class Bolhas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2*32, 15*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 64
        self.rect.y = 352
class Amuleto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*32, 15*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 96
        self.rect.y = 352
class Anel1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4*32, 15*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 128
        self.rect.y = 352
class Anel2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5*32, 15*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 352
class Colar1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 15*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 192
        self.rect.y = 352
class Colar2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 15*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 224
        self.rect.y = 352


lista_itens = pygame.sprite.Group()
lista_bau_aberto = pygame.sprite.Group()
lista_bau_fechado = pygame.sprite.Group()
bau_fechado = BauFechado()
bau_aberto = BauAberto()
chave1 = Chave1()
chave2 = Chave2()
chave3 = Chave3()
chave4 = Chave4()
chave5 = Chave5()
chave6 = Chave6()
pocao1 = Pocao1()
pocao2 = Pocao2()
pocao3 = Pocao3()
pocao4 = Pocao4()
pocao5 = Pocao5()
pocao6 = Pocao6()
pocao7 = Pocao7()
pocao8 = Pocao8()
papeis = Papeis()
pergaminho = Pergaminho()
rolo_pergaminho = RoloPergaminho()
mapa = Mapa()
livro_aberto1 = LivroAberto1()
livro_aberto2 = LivroAberto2()
livro_fechado1 = LivroFechado1()
livro_fechado2 = LivroFechado2()
espada1 = Espada1()
espada2 = Espada2()
espada3 = Espada3()
espada4 = Espada4()
espada5 = Espada5()
espada6 = Espada6()
espada7 = Espada7()
espada8 = Espada8()
machado1 = Machado1()
machado2 = Machado2()
machado3 = Machado3()
machado4 = Machado4()
machado5 = Machado5()
machado6 = Machado6()
machado7 = Machado7()
machado8 = Machado8()
shuriken1 = Shuriken1()
shuriken2 = Shuriken2()
espadas = Espadas()
arco1 = Arco1()
arco2 = Arco2()
arco3 = Arco3()
crossbow1 = Crossbow1()
crossbow2 = Crossbow2()
minibomba = MiniBomba()
bombamedia = BombaMedia()
bombagrande = BombaGrande()
miniflecha = Miniflecha()
flechamedia = FlechaMedia()
flechagrande = FlechaGrande()
dardos1 = Dardos1()
dardos2 = Dardos2()
armadura1 = Armadura1()
armadura2 = Armadura2()
armadura3 = Armadura3()
armadura4 = Armadura4()
armadura5 = Armadura5()
armadura6 = Armadura6()
armadura7 = Armadura7()
armadura8 = Armadura8()
capacete1 = Capacete1()
capacete2 = Capacete2()
capacete3 = Capacete3()
capacete4 = Capacete4()
capacete5 = Capacete5()
capacete6 = Capacete6()
capacete7 = Capacete7()
capacete8 = Capacete8()
escudo1 = Escudo1()
escudo2 = Escudo2()
escudo3 = Escudo3()
escudo4 = Escudo4()
escudo5 = Escudo5()
escudo6 = Escudo6()
escudo7 = Escudo7()
escudo8 = Escudo8()
cajado1 = Cajado1()
cajado2 = Cajado2()
cajado3 = Cajado3()
cajado4 = Cajado4()
cajado5 = Cajado5()
cajado6 = Cajado6()
cajado7 = Cajado7()
cajado8 = Cajado8()
poucas_moedas = PoucasMoedas()
muitas_moedas = MuitasMoedas()
bolhas = Bolhas()
amuleto = Amuleto()
anel1 = Anel1()
anel2 = Anel2()
colar1 = Colar1()
colar2 = Colar2()
lista_bau_aberto.add(bau_aberto)
lista_bau_fechado.add(bau_fechado)
lista_itens.add(bau_fechado)
lista_itens.add(bau_aberto)
lista_itens.add(chave1)
lista_itens.add(chave2)
lista_itens.add(chave3)
lista_itens.add(chave4)
lista_itens.add(chave5)
lista_itens.add(chave6)
lista_itens.add(pocao1)
lista_itens.add(pocao2)
lista_itens.add(pocao3)
lista_itens.add(pocao4)
lista_itens.add(pocao5)
lista_itens.add(pocao6)
lista_itens.add(pocao7)
lista_itens.add(pocao8)
lista_itens.add(papeis)
lista_itens.add(pergaminho)
lista_itens.add(rolo_pergaminho)
lista_itens.add(mapa)
lista_itens.add(livro_aberto1)
lista_itens.add(livro_aberto2)
lista_itens.add(livro_fechado1)
lista_itens.add(livro_fechado2)
lista_itens.add(espada1)
lista_itens.add(espada2)
lista_itens.add(espada3)
lista_itens.add(espada4)
lista_itens.add(espada5)
lista_itens.add(espada6)
lista_itens.add(espada7)
lista_itens.add(espada8)
lista_itens.add(machado1)
lista_itens.add(machado2)
lista_itens.add(machado3)
lista_itens.add(machado4)
lista_itens.add(machado5)
lista_itens.add(machado6)
lista_itens.add(machado7)
lista_itens.add(machado8)
lista_itens.add(shuriken1)
lista_itens.add(shuriken2)
lista_itens.add(espadas)
lista_itens.add(arco1)
lista_itens.add(arco2)
lista_itens.add(arco3)
lista_itens.add(crossbow1)
lista_itens.add(crossbow2)
lista_itens.add(minibomba)
lista_itens.add(bombamedia)
lista_itens.add(bombagrande)
lista_itens.add(miniflecha)
lista_itens.add(flechamedia)
lista_itens.add(flechagrande)
lista_itens.add(dardos1)
lista_itens.add(dardos2)
lista_itens.add(armadura1)
lista_itens.add(armadura2)
lista_itens.add(armadura3)
lista_itens.add(armadura4)
lista_itens.add(armadura5)
lista_itens.add(armadura6)
lista_itens.add(armadura7)
lista_itens.add(armadura8)
lista_itens.add(capacete1)
lista_itens.add(capacete2)
lista_itens.add(capacete3)
lista_itens.add(capacete4)
lista_itens.add(capacete5)
lista_itens.add(capacete6)
lista_itens.add(capacete7)
lista_itens.add(capacete8)
lista_itens.add(escudo1)
lista_itens.add(escudo2)
lista_itens.add(escudo3)
lista_itens.add(escudo4)
lista_itens.add(escudo5)
lista_itens.add(escudo6)
lista_itens.add(escudo7)
lista_itens.add(escudo8)
lista_itens.add(cajado1)
lista_itens.add(cajado2)
lista_itens.add(cajado3)
lista_itens.add(cajado4)
lista_itens.add(cajado5)
lista_itens.add(cajado6)
lista_itens.add(cajado7)
lista_itens.add(cajado8)
lista_itens.add(poucas_moedas)
lista_itens.add(muitas_moedas)
lista_itens.add(bolhas)
lista_itens.add(amuleto)
lista_itens.add(anel1)
lista_itens.add(anel2)
lista_itens.add(colar1)
lista_itens.add(colar2)
