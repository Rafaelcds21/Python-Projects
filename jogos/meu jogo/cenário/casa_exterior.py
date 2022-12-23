import os

pygame.init()


class Parede1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 64)


class Parede2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 64)


class Parede3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 64)


class Parede4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 64)


class Parede5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 64)


class Parede6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 96)


class Parede7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 96)


class Parede8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (192, 96)


class Parede9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (224, 96)


class Porta1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 96)


class Pilar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0 * 32, 3 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 64)


class Telhado1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0 * 32, 1 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 160)


class Telhado2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1 * 32, 1 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (32, 160)


class Telhado3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((2 * 32, 1 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64, 160)


class Telhado4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (96, 160)


class Telhado5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((1 * 32, 2 * 32), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (128, 160)

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, '../conjunto imagens')
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'fantasy-tileset.png'))

tela = pygame.display.set_mode((512, 320))

lista_casa_exterior = pygame.sprite.Group()
parede1 = Parede1()
parede2 = Parede2()
parede3 = Parede3()
parede4 = Parede4()
parede5 = Parede5()
parede6 = Parede6()
parede7 = Parede7()
parede8 = Parede8()
parede9 = Parede9()
porta1 = Porta1()
# pilar = Pilar()
# telhado1 = Telhado1()
# telhado2 = Telhado2()
# telhado3 = Telhado3()
# telhado4 = Telhado4()
# telhado5 = Telhado5()
lista_casa_exterior.add(parede1)
lista_casa_exterior.add(parede2)
lista_casa_exterior.add(parede3)
lista_casa_exterior.add(parede4)
lista_casa_exterior.add(parede5)
lista_casa_exterior.add(parede6)
lista_casa_exterior.add(parede7)
lista_casa_exterior.add(parede8)
lista_casa_exterior.add(parede9)
lista_casa_exterior.add(porta1)
# lista_casa_exterior.add(pilar)
# lista_casa_exterior.add(telhado1)
# lista_casa_exterior.add(telhado2)
# lista_casa_exterior.add(telhado3)
# lista_casa_exterior.add(telhado4)
# lista_casa_exterior.add(telhado5)

while True:
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    lista_casa_exterior.draw(tela)
    lista_casa_exterior.update()

    pygame.display.update()
