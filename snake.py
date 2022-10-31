import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

x_snake = 510
y_snake = 350

x_apple = randint(0, 1010)
y_apple = randint(0, 690)

score = 0

fonte = pygame.font.SysFont('arial', 30, True, True)

tela = pygame.display.set_mode((1020, 700))
título = pygame.display.set_caption('Snake')
relógio = pygame.time.Clock()

lista_cobra = []

comprimento_inicial = 5

velocidade = 7
x_controle = velocidade
y_controle = 0

morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x,y]
        #XeY[0] = x
        #XeY[1] = y
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 10, 10))

def reiniciar_jogo():
    global score, comprimento_inicial, x_snake, y_snake, lista_cobra, lista_cabeça, x_apple, y_apple, morreu
    score = 0
    comprimento_inicial = 5
    x_snake = 510
    y_snake = 350
    lista_cobra = []
    lista_cabeça = []
    x_apple = randint(0, 1010)
    y_apple = randint(0, 690)
    morreu = False

while True:
    relógio.tick(30)
    tela.fill((255, 255, 255))

    mensagem = f'Score: {score}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

    x_snake = x_snake + x_controle
    y_snake = y_snake + y_controle

    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 10, 10))
    apple = pygame.draw.rect(tela, (255, 0, 0), (x_apple, y_apple, 10, 10))

    if snake.colliderect(apple):
        x_apple = randint(0, 1010)
        y_apple = randint(0, 690)

        score += 1

        comprimento_inicial += 1

    lista_cabeça = []
    lista_cabeça.append(x_snake)
    lista_cabeça.append(y_snake)
    lista_cobra.append(lista_cabeça)

    if lista_cobra.count(lista_cabeça) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para reiniciar'
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))

        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            tela.blit(texto_formatado, (310, 350))
            pygame.display.update()

    if x_snake > 1020:
        x_snake = 0
    if x_snake < 0:
        x_snake = 1020
    if y_snake > 700:
        y_snake = 0
    if y_snake < 0:
        y_snake = 700

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (830, 50))

    pygame.display.update()
