import pygame
import os

pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, '../conjunto imagens')
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'fantasy-tileset.png'))


class Ceu1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)


class Ceu2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 0)


class Ceu3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 0)


class Ceu4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 0)


class Ceu5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 0)


class Ceu6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 0)


class Ceu7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 0)


class Ceu8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 0)


class Ceu9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 32)


class Ceu10(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 32)


class Ceu11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 32)


class Ceu12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 32)


class Ceu13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 32)


class Ceu14(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 32)


class Ceu15(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 32)


class Ceu16(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 32)


class Ceu17(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 64)


class Ceu18(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 64)


class Ceu19(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 64)


class Ceu20(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 64)


class Ceu21(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 64)


class Ceu22(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 64)


class Ceu23(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 64)


class Ceu24(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 64)


class Ceu25(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (256, 0)


class Ceu26(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (288, 0)


class Ceu27(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 0)


class Ceu28(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (352, 0)


class Ceu29(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (384, 0)


class Ceu30(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (416, 0)


class Ceu31(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (448, 0)


class Ceu32(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (480, 0)


class Ceu33(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (256, 32)


class Ceu34(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (288, 32)


class Ceu35(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 32)


class Ceu36(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (352, 32)


class Ceu37(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (384, 32)


class Ceu38(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (416, 32)


class Ceu39(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (448, 32)


class Ceu40(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (480, 32)


class Ceu41(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (256, 64)


class Ceu42(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (288, 64)


class Ceu43(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 64)


class Ceu44(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (352, 64)


class Ceu45(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (384, 64)


class Ceu46(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (416, 64)


class Ceu47(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (448, 64)


class Ceu48(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32, 3*32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (480, 64)


lista_mapa = pygame.sprite.Group()
ceu1 = Ceu1()
ceu2 = Ceu2()
ceu3 = Ceu3()
ceu4 = Ceu4()
ceu5 = Ceu5()
ceu6 = Ceu6()
ceu7 = Ceu7()
ceu8 = Ceu8()
ceu9 = Ceu9()
ceu10 = Ceu10()
ceu11 = Ceu11()
ceu12 = Ceu12()
ceu13 = Ceu13()
ceu14 = Ceu14()
ceu15 = Ceu15()
ceu16 = Ceu16()
ceu17 = Ceu17()
ceu18 = Ceu18()
ceu19 = Ceu19()
ceu20 = Ceu20()
ceu21 = Ceu21()
ceu22 = Ceu22()
ceu23 = Ceu23()
ceu24 = Ceu24()
ceu25 = Ceu25()
ceu26 = Ceu26()
ceu27 = Ceu27()
ceu28 = Ceu28()
ceu29 = Ceu29()
ceu30 = Ceu30()
ceu31 = Ceu31()
ceu32 = Ceu32()
ceu33 = Ceu33()
ceu34 = Ceu34()
ceu35 = Ceu35()
ceu36 = Ceu36()
ceu37 = Ceu37()
ceu38 = Ceu38()
ceu39 = Ceu39()
ceu40 = Ceu40()
ceu41 = Ceu41()
ceu42 = Ceu42()
ceu43 = Ceu43()
ceu44 = Ceu44()
ceu45 = Ceu45()
ceu46 = Ceu46()
ceu47 = Ceu47()
ceu48 = Ceu48()
lista_mapa.add(ceu1)
lista_mapa.add(ceu2)
lista_mapa.add(ceu3)
lista_mapa.add(ceu4)
lista_mapa.add(ceu5)
lista_mapa.add(ceu6)
lista_mapa.add(ceu7)
lista_mapa.add(ceu8)
lista_mapa.add(ceu9)
lista_mapa.add(ceu10)
lista_mapa.add(ceu11)
lista_mapa.add(ceu12)
lista_mapa.add(ceu13)
lista_mapa.add(ceu14)
lista_mapa.add(ceu15)
lista_mapa.add(ceu16)
lista_mapa.add(ceu17)
lista_mapa.add(ceu18)
lista_mapa.add(ceu19)
lista_mapa.add(ceu20)
lista_mapa.add(ceu21)
lista_mapa.add(ceu22)
lista_mapa.add(ceu23)
lista_mapa.add(ceu24)
lista_mapa.add(ceu25)
lista_mapa.add(ceu26)
lista_mapa.add(ceu27)
lista_mapa.add(ceu28)
lista_mapa.add(ceu29)
lista_mapa.add(ceu30)
lista_mapa.add(ceu31)
lista_mapa.add(ceu32)
lista_mapa.add(ceu33)
lista_mapa.add(ceu34)
lista_mapa.add(ceu35)
lista_mapa.add(ceu36)
lista_mapa.add(ceu37)
lista_mapa.add(ceu38)
lista_mapa.add(ceu39)
lista_mapa.add(ceu40)
lista_mapa.add(ceu41)
lista_mapa.add(ceu42)
lista_mapa.add(ceu43)
lista_mapa.add(ceu44)
lista_mapa.add(ceu45)
lista_mapa.add(ceu46)
lista_mapa.add(ceu47)
lista_mapa.add(ceu48)
