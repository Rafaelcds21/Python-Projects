import pygame
import os

pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, '../conjunto imagens')
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'fantasy-tileset.png'))


class Chao1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 224)


class Chao2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 224)


class Chao3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 224)


class Chao4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 224)


class Chao5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 224)


class Chao6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 224)


class Chao7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 224)


class Chao8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 224)


class Chao17(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 160)


class Chao18(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 160)


class Chao19(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 160)


class Chao20(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 160)


class Chao21(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 160)


class Chao22(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 160)


class Chao23(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 160)


class Chao24(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 160)


class Chao25(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 128)


class Chao26(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 128)


class Chao27(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 128)


class Chao28(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 128)


class Chao29(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 128)


class Chao30(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 128)


class Chao31(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 128)


class Chao32(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 128)


class Chao33(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 96)


class Chao34(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 96)


class Chao35(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 96)


class Chao36(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 96)


class Chao37(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 96)


class Chao38(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 96)


class Chao39(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 96)


class Chao40(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 96)


class Chao41(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (256, 224)


class Chao42(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (288, 224)


class Chao43(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 224)


class Chao44(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (352, 224)


class Chao45(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (384, 224)


class Chao46(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (416, 224)


class Chao47(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (448, 224)


class Chao48(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (480, 224)


class Chao49(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (256, 192)


class Chao50(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (288, 192)


class Chao51(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 192)


class Chao52(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (352, 192)


class Chao53(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (384, 192)


class Chao54(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (416, 192)


class Chao55(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (448, 192)


class Chao56(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (480, 192)


class Chao57(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (256, 160)


class Chao58(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (288, 160)


class Chao59(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 160)


class Chao60(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (352, 160)


class Chao61(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (384, 160)


class Chao62(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (416, 160)


class Chao63(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (448, 160)


class Chao64(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (480, 160)


class Chao65(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (256, 128)


class Chao66(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (288, 128)


class Chao67(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 128)


class Chao68(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (352, 128)


class Chao69(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (384, 128)


class Chao70(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (416, 128)


class Chao71(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (448, 128)


class Chao72(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (480, 128)


class Chao73(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (256, 96)


class Chao74(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (288, 96)


class Chao75(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 96)


class Chao76(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (352, 96)


class Chao77(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (384, 96)


class Chao78(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (416, 96)


class Chao79(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (448, 96)


class Chao80(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (480, 96)


class Chao81(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 256)


class Chao82(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 256)


class Chao83(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 256)


class Chao84(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 256)


class Chao85(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 256)


class Chao86(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 256)


class Chao87(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 256)


class Chao88(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 256)


class Chao89(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (256, 256)


class Chao90(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (288, 256)


class Chao91(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 256)


class Chao92(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (352, 256)


class Chao93(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (384, 256)


class Chao94(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (416, 256)


class Chao95(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (448, 256)


class Chao96(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (480, 256)


class Chao97(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 288)


class Chao98(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 288)


class Chao99(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 288)


class Chao100(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 288)


class Chao101(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 288)


class Chao102(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 288)


class Chao103(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 288)


class Chao104(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 288)


class Chao105(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (256, 288)


class Chao106(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (288, 288)


class Chao107(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (320, 288)


class Chao108(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (352, 288)


class Chao109(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (384, 288)


class Chao110(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (416, 288)


class Chao111(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (448, 288)


class Chao112(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (480, 288)


class Estrada1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 192)


class Estrada2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 192)


class Estrada3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 192)


class Estrada4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 192)


class Estrada5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 192)


class Estrada6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 192)


class Estrada7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 192)


class Estrada8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((4 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 192)


lista_mapa = pygame.sprite.Group()
chao1 = Chao1()
chao2 = Chao2()
chao3 = Chao3()
chao4 = Chao4()
chao5 = Chao5()
chao6 = Chao6()
chao7 = Chao7()
chao8 = Chao8()
chao17 = Chao17()
chao18 = Chao18()
chao19 = Chao19()
chao20 = Chao20()
chao21 = Chao21()
chao22 = Chao22()
chao23 = Chao23()
chao24 = Chao24()
chao25 = Chao25()
chao26 = Chao26()
chao27 = Chao27()
chao28 = Chao28()
chao29 = Chao29()
chao30 = Chao30()
chao31 = Chao31()
chao32 = Chao32()
chao33 = Chao33()
chao34 = Chao34()
chao35 = Chao35()
chao36 = Chao36()
chao37 = Chao37()
chao38 = Chao38()
chao39 = Chao39()
chao40 = Chao40()
chao41 = Chao41()
chao42 = Chao42()
chao43 = Chao43()
chao44 = Chao44()
chao45 = Chao45()
chao46 = Chao46()
chao47 = Chao47()
chao48 = Chao48()
chao49 = Chao49()
chao50 = Chao50()
chao51 = Chao51()
chao52 = Chao52()
chao53 = Chao53()
chao54 = Chao54()
chao55 = Chao55()
chao56 = Chao56()
chao57 = Chao57()
chao58 = Chao58()
chao59 = Chao59()
chao60 = Chao60()
chao61 = Chao61()
chao62 = Chao62()
chao63 = Chao63()
chao64 = Chao64()
chao65 = Chao65()
chao66 = Chao66()
chao67 = Chao67()
chao68 = Chao68()
chao69 = Chao69()
chao70 = Chao70()
chao71 = Chao71()
chao72 = Chao72()
chao73 = Chao73()
chao74 = Chao74()
chao75 = Chao75()
chao76 = Chao76()
chao77 = Chao77()
chao78 = Chao78()
chao79 = Chao79()
chao80 = Chao80()
chao81 = Chao81()
chao82 = Chao82()
chao83 = Chao83()
chao84 = Chao84()
chao85 = Chao85()
chao86 = Chao86()
chao87 = Chao87()
chao88 = Chao88()
chao89 = Chao89()
chao90 = Chao90()
chao91 = Chao91()
chao92 = Chao92()
chao93 = Chao93()
chao94 = Chao94()
chao95 = Chao95()
chao96 = Chao96()
chao97 = Chao97()
chao98 = Chao98()
chao99 = Chao99()
chao100 = Chao100()
chao101 = Chao101()
chao102 = Chao102()
chao103 = Chao103()
chao104 = Chao104()
chao105 = Chao105()
chao106 = Chao106()
chao107 = Chao107()
chao108 = Chao108()
chao109 = Chao109()
chao110 = Chao110()
chao111 = Chao111()
chao112 = Chao112()
estrada1 = Estrada1()
estrada2 = Estrada2()
estrada3 = Estrada3()
estrada4 = Estrada4()
estrada5 = Estrada5()
estrada6 = Estrada6()
estrada7 = Estrada7()
estrada8 = Estrada8()
lista_mapa.add(chao1)
lista_mapa.add(chao2)
lista_mapa.add(chao3)
lista_mapa.add(chao4)
lista_mapa.add(chao5)
lista_mapa.add(chao6)
lista_mapa.add(chao7)
lista_mapa.add(chao8)
lista_mapa.add(chao17)
lista_mapa.add(chao18)
lista_mapa.add(chao19)
lista_mapa.add(chao20)
lista_mapa.add(chao21)
lista_mapa.add(chao22)
lista_mapa.add(chao23)
lista_mapa.add(chao24)
lista_mapa.add(chao25)
lista_mapa.add(chao26)
lista_mapa.add(chao27)
lista_mapa.add(chao28)
lista_mapa.add(chao29)
lista_mapa.add(chao30)
lista_mapa.add(chao31)
lista_mapa.add(chao32)
lista_mapa.add(chao33)
lista_mapa.add(chao34)
lista_mapa.add(chao35)
lista_mapa.add(chao36)
lista_mapa.add(chao37)
lista_mapa.add(chao38)
lista_mapa.add(chao39)
lista_mapa.add(chao40)
lista_mapa.add(chao41)
lista_mapa.add(chao42)
lista_mapa.add(chao43)
lista_mapa.add(chao44)
lista_mapa.add(chao45)
lista_mapa.add(chao46)
lista_mapa.add(chao47)
lista_mapa.add(chao48)
lista_mapa.add(chao49)
lista_mapa.add(chao50)
lista_mapa.add(chao51)
lista_mapa.add(chao52)
lista_mapa.add(chao53)
lista_mapa.add(chao54)
lista_mapa.add(chao55)
lista_mapa.add(chao56)
lista_mapa.add(chao57)
lista_mapa.add(chao58)
lista_mapa.add(chao59)
lista_mapa.add(chao60)
lista_mapa.add(chao61)
lista_mapa.add(chao62)
lista_mapa.add(chao63)
lista_mapa.add(chao64)
lista_mapa.add(chao65)
lista_mapa.add(chao66)
lista_mapa.add(chao67)
lista_mapa.add(chao68)
lista_mapa.add(chao69)
lista_mapa.add(chao70)
lista_mapa.add(chao71)
lista_mapa.add(chao72)
lista_mapa.add(chao73)
lista_mapa.add(chao74)
lista_mapa.add(chao75)
lista_mapa.add(chao76)
lista_mapa.add(chao77)
lista_mapa.add(chao78)
lista_mapa.add(chao79)
lista_mapa.add(chao80)
lista_mapa.add(chao81)
lista_mapa.add(chao82)
lista_mapa.add(chao83)
lista_mapa.add(chao84)
lista_mapa.add(chao85)
lista_mapa.add(chao86)
lista_mapa.add(chao87)
lista_mapa.add(chao88)
lista_mapa.add(chao89)
lista_mapa.add(chao90)
lista_mapa.add(chao91)
lista_mapa.add(chao92)
lista_mapa.add(chao93)
lista_mapa.add(chao94)
lista_mapa.add(chao95)
lista_mapa.add(chao96)
lista_mapa.add(chao97)
lista_mapa.add(chao98)
lista_mapa.add(chao99)
lista_mapa.add(chao100)
lista_mapa.add(chao101)
lista_mapa.add(chao102)
lista_mapa.add(chao103)
lista_mapa.add(chao104)
lista_mapa.add(chao105)
lista_mapa.add(chao106)
lista_mapa.add(chao107)
lista_mapa.add(chao108)
lista_mapa.add(chao109)
lista_mapa.add(chao110)
lista_mapa.add(chao111)
lista_mapa.add(chao112)
lista_mapa.add(estrada1)
lista_mapa.add(estrada2)
lista_mapa.add(estrada3)
lista_mapa.add(estrada4)
lista_mapa.add(estrada5)
lista_mapa.add(estrada6)
lista_mapa.add(estrada7)
lista_mapa.add(estrada8)
