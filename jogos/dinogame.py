import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

pygame.init()
pygame.mixer.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

tela = pygame.display.set_mode((640, 480))
nome_do_jogo = pygame.display.set_caption('Dinogame')
relogio = pygame.time.Clock()

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'dino game.png')).convert_alpha()

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'morreu.wav'))
som_colisao.set_volume(1)

som_pontuaçao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'morreu.wav'))
som_pontuaçao.set_volume(1)

colidiu = False

escolha_obstaculo = choice([0, 1])

pontos = 0

velociade_jogo = 7


def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado


def reiniciar_jogo():
    global pontos, velociade_jogo, colidiu, escolha_obstaculo
    pontos = 0
    velociade_jogo = 10
    colidiu = False
    dino.rect.y = 426
    dino.pulo = False
    cacto.rect.x = 640
    dino_voador.rect.x = 640
    escolha_obstaculo = choice([0, 1])


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'pulo.wav'))
        self.som_pulo.set_volume(0.3)
        self.imagens_dinossauro = []
        for i in range(3):
            img = sprite_sheet.subsurface((i*32, 0), (32, 32))# (x, y), (largura, altura)
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauro.append(img)

        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = 426 - 48
        self.rect.center = (100, 426)
        self.pulo = False

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def update(self):
        if self.pulo == True:
            if self.rect.y <= 200:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20

            else:
                self.rect.y = self.pos_y_inicial

        if self.index_lista >= 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.index_lista)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((224, 0), (32, 32)) #7*32=224
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = 640 - randrange(30, 300, 90)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = 640
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= velociade_jogo

class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6*32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.y = 480 - 64
        self.rect.x = pos_x * 64

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = 640
        self.rect.x -= 7


class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (96, 96))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (640, 480-60)
        self.rect.x = 640

    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
               self.rect_x = 640
            self.rect.x -= velociade_jogo


class DinoVoador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        for i in range(3, 5):
            img = sprite_sheet.subsurface((i*32, 0), (32, 32))
            img = pygame.transform.scale(img, (96, 96))
            self.imagens_dinossauro.append(img)

        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect = self.image.get_rect()
        self.rect.center = (640, 300)
        self.rect.x = 640

    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = 640
            self.rect.x -= velociade_jogo

            if self.index_lista >= 1:
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.imagens_dinossauro[int(self.index_lista)]


todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)

for i in range(4):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

for i in range(640*2//64):
 chao = Chao(i)
 todas_as_sprites.add(chao)

cacto = Cacto()
todas_as_sprites.add(cacto)

grupo_obstáculos = pygame.sprite.Group()
grupo_obstáculos.add(cacto)

dino_voador = DinoVoador()
todas_as_sprites.add(dino_voador)
grupo_obstáculos.add(dino_voador)

while True:
    relogio.tick(30)
    tela.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE and colidiu == False:
                if dino.rect.y != dino.pos_y_inicial:
                    pass
                else:
                    dino.pular()

            if event.key == K_r and colidiu == True:
                reiniciar_jogo()

    colisoes = pygame.sprite.spritecollide(dino, grupo_obstáculos, False, pygame.sprite.collide_mask)

    todas_as_sprites.draw(tela)

    if cacto.rect.topright[0] <= 0 or dino_voador.rect.topright[0] <= 0:
        escolha_obstaculo = choice([0, 1])
        cacto.rect.x = 640
        dino_voador.rect.x = 640
        cacto.escolha = escolha_obstaculo
        dino_voador.escolha = escolha_obstaculo

    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True

    if colidiu == True:
        if pontos % 100 == 0:
            pontos += 1

        game_over = exibe_mensagem('GAME OVER!', 40, (0, 0, 0))
        tela.blit(game_over, (320, 240))
        restart = exibe_mensagem('Pressione r para reiniciar', 20, (0, 0, 0))
        tela.blit(restart, (320, 300))

    else:
        pontos += 1
        todas_as_sprites.update()
        texto_pontos = exibe_mensagem(pontos, 40, (0, 0, 0))

    if pontos % 100 == 0:
        som_pontuaçao.play()
        if velociade_jogo >= 23:
            velociade_jogo += 0
        else:
            velociade_jogo += 1

    tela.blit(texto_pontos, (520, 30))

    pygame.display.flip()
