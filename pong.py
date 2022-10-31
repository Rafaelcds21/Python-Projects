import pygame
from pygame.locals import *
from sys import exit
from random import randrange

# PROBLEMA 1: Eixo y não está variando direito
# PROBLEMA 2: resolver a questão da pontuação, ou está dando 3 ou erro

pygame.init()


def reiniciar_jogo():
    global score1, score2, x_bola, y_bola, x_raquete1, y_raquete1, x_raquete2, y_raquete2, morreu
    score1 = 0
    score2 = 0
    x_bola = 512
    y_bola = 350
    x_raquete1 = 100
    y_raquete1 = 100
    x_raquete2 = 925
    y_raquete2 = 100
    morreu = False


x_raquete1 = 100
y_raquete1 = 100
compx_raquete1 = 10
compy_raquete1 = 30

x_raquete2 = 925
y_raquete2 = 100
compx_raquete2 = 10
compy_raquete2 = 30

x_bola = 512
y_bola = 350
velocidadex = 5
velocidadey = randrange(-1, 1)

Largura = 1025
Altura = 700

tela = pygame.display.set_mode((Largura, Altura))
nome_do_jogo = pygame.display.set_caption('pong')
relogio = pygame.time.Clock()

fonte = pygame.font.SysFont('arial', 30, True, True)

score1 = 0
score2 = 0

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))

    mensagem1 = f'{score1}'
    texto_formatado1 = fonte.render(mensagem1, True, (255, 255, 255))

    mensagem2 = f'{score2}'
    texto_formatado2 = fonte.render(mensagem2, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # movimento da raquete
    if pygame.key.get_pressed()[K_w]:
        y_raquete1 -= 10
    if pygame.key.get_pressed()[K_s]:
        y_raquete1 += 10
    if pygame.key.get_pressed()[K_i]:
        y_raquete2 -= 10
    if pygame.key.get_pressed()[K_k]:
        y_raquete2 += 10

    # se as raquetes sair da tela ela volta
    if y_raquete1 > 700:
        y_raquete1 = 670
    if y_raquete1 < 0:
        y_raquete1 = 0

    if y_raquete2 > 700:
        y_raquete2 = 670
    if y_raquete2 < 0:
        y_raquete2 = 0

    # se a bola sair da tela reinicia
    if y_bola > 700 or y_bola < 0 or x_bola > 1025 or y_bola < 0:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para reiniciar'
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))

        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            tela.blit(texto_formatado, (310, 350))
            pygame.display.update()

    # criando a raquete, a bola e a divisória
    raquete1 = pygame.draw.rect(tela, (255, 255, 255), (x_raquete1, y_raquete1, compx_raquete1, compy_raquete1))
    raquete2 = pygame.draw.rect(tela, (255, 255, 255), (x_raquete2, y_raquete2, compx_raquete2, compy_raquete2))
    bola = pygame.draw.circle(tela, (255, 255, 255), (x_bola, y_bola), 10)
    divisoria = pygame.draw.line(tela, (255, 255, 255), (512, 0), (512, 700))

    # if bola.collidepoint(x_raquete1, y_raquete1):
    # score1 += 1

    # if bola.collidepoint(x_raquete2, y_raquete2):
    # score2 += 1

    if bola.colliderect(raquete2):
        velocidadex = -velocidadex
        score2 += 1

    if bola.colliderect(raquete1):
        velocidadex = -velocidadex
        score1 += 1

    x_bola += velocidadex
    y_bola += velocidadey

    tela.blit(texto_formatado1, (100, 50))

    tela.blit(texto_formatado2, (925, 50))

    pygame.display.flip()
