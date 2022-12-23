import pygame
from pygame.locals import *
from sys import exit
from cenário import casainterior, ceu, chao
from player import players, fichaplayer
import itens
from inimigos import inimigos
import avanco

pygame.init()


def tela1():
    fonte = pygame.font.Font('freesansbold.ttf', 16)
    texto1 = fonte.render('Busca pela esfera', True, (0, 255, 0))
    texto2 = fonte.render('Olá, viajante. Que bom que você', True, (0, 255, 0))
    texto3 = fonte.render('está aqui. Roubaram uma esfera', True, (0, 255, 0))
    texto4 = fonte.render('de extrema importância', True, (0, 255, 0))
    texto5 = fonte.render('Você pode me ajudar?', True, (0, 255, 0))

    tela.blit(texto1, (0, 0))
    tela.blit(texto2, (0, 20))
    tela.blit(texto3, (0, 40))
    tela.blit(texto4, (0, 60))
    tela.blit(texto5, (0, 80))


tela = pygame.display.set_mode((512, 320))

nome = pygame.display.set_caption('tela de início')

fonte = pygame.font.Font('freesansbold.ttf', 16)

sim = fonte.render('sim', True, (255, 255, 255))
nao = fonte.render('não', True, (255, 255, 255))

texto6 = fonte.render('Perdão pela rapidez, devemos', True, (0, 255, 0))
texto7 = fonte.render('nos apresentar, quem é você?', True, (0, 255, 0))

texto8 = fonte.render('Muito bem, é só seguir a estrada', True, (0, 255, 0))
texto9 = fonte.render('principal para seguir o rastro dos', True, (0, 255, 0))
texto10 = fonte.render('ladrões', True, (0, 255, 0))
texto11 = fonte.render('Continuar', True, (255, 255, 255))

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mouse = pygame.mouse.get_pos()
    tela1()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            if 0 <= mouse[0] <= 90 and 80 <= mouse[1] <= 120:
                while True:
                    tela.fill((0, 0, 0))
                    mouse = pygame.mouse.get_pos()

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()

                        if event.type == MOUSEBUTTONDOWN:
                            if 0 <= mouse[0] <= 32 and 40 <= mouse[1] <= 72:
                                avanco.avanco_goblin_guerreiro()

                            if 32 <= mouse[0] <= 64 and 40 <= mouse[1] <= 72:
                                avanco.avanco_humano_guerreiro()

                            if 64 <= mouse[0] <= 96 and 40 <= mouse[1] <= 72:
                                avanco.avanco_meio_orc_guerreiro()

                            if 96 <= mouse[0] <= 128 and 40 <= mouse[1] <= 72:
                                avanco.avanco_elfo_guerreiro()

                            if 128 <= mouse[0] <= 160 and 40 <= mouse[1] <= 72:
                                avanco.avanco_arqueiro()

                            if 160 <= mouse[0] <= 192 and 40 <= mouse[1] <= 72:
                                avanco.avanco_paladino()

                            if 192 <= mouse[0] <= 224 and 40 <= mouse[1] <= 72:
                                avanco.avanco_mago()

                            if 224 <= mouse[0] <= 256 and 40 <= mouse[1] <= 72:
                                avanco.avanco_feiticeiro()

                                tela.blit(texto8, (0, 0))
                                tela.blit(texto9, (0, 20))
                                tela.blit(texto10, (0, 40))

                                if 0 <= mouse[0] <= 256 and 60 <= mouse[1] <= 100:
                                    pygame.draw.rect(tela, (170, 170, 170), [0, 60, 256, 40])

                                else:
                                    pygame.draw.rect(tela, (100, 100, 100), [0, 60, 256, 40])

                                tela.blit(texto11, (85, 70))

                                pygame.display.update()

                    tela.blit(texto6, (0, 0))
                    tela.blit(texto7, (0, 20))

                    if 0 <= mouse[0] <= 32 and 40 <= mouse[1] <= 72:
                        pygame.draw.rect(tela, (170, 170, 170), [0, 40, 32, 32])
                        fichaplayer.fichagoblinguerreiro()

                    #elif 32 <= mouse[0] <= 64 and 40 <= mouse[1] <= 72:
                        #pygame.draw.rect(tela, (170, 170, 170), [32, 40, 32, 32])
                        #fichaplayer.fichahumanoguerreiro()

                    #elif 64 <= mouse[0] <= 96 and 40 <= mouse[1] <= 72:
                        #pygame.draw.rect(tela, (170, 170, 170), [64, 40, 32, 32])
                        #fichaplayer.fichameioorcguerreiro()

                    #elif 96 <= mouse[0] <= 128 and 40 <= mouse[1] <= 72:
                        #pygame.draw.rect(tela, (170, 170, 170), [96, 40, 32, 32])
                        #fichaplayer.fichaelfoguerreiro()

                    #elif 128 <= mouse[0] <= 160 and 40 <= mouse[1] <= 72:
                        #pygame.draw.rect(tela, (170, 170, 170), [128, 40, 32, 32])
                        #fichaplayer.fichaarqueiro()

                    #elif 160 <= mouse[0] <= 192 and 40 <= mouse[1] <= 72:
                        #pygame.draw.rect(tela, (170, 170, 170), [160, 40, 32, 32])
                        #fichaplayer.fichapaladino()

                    #elif 192 <= mouse[0] <= 224 and 40 <= mouse[1] <= 72:
                        #pygame.draw.rect(tela, (170, 170, 170), [192, 40, 32, 32])
                        #fichaplayer.fichamago()

                    #elif 224 <= mouse[0] <= 256 and 40 <= mouse[1] <= 72:
                        #pygame.draw.rect(tela, (170, 170, 170), [224, 40, 32, 32])
                        #fichaplayer.fichafeiticeiro()

                    players.lista_player.draw(tela)
                    players.lista_player.update()

                    pygame.display.update()

            elif 110 <= mouse[0] <= 200 and 100 <= mouse[1] <= 120:
                pygame.quit()

    if 0 <= mouse[0] <= 90 and 100 <= mouse[1] <= 140:
        pygame.draw.rect(tela, (170, 170, 170), [0, 100, 90, 40])

    else:
        pygame.draw.rect(tela, (100, 100, 100), [0, 100, 90, 40])

    if 110 <= mouse[0] <= 200 and 100 <= mouse[1] <= 140:
        pygame.draw.rect(tela, (170, 170, 170), [110, 100, 90, 40])

    else:
        pygame.draw.rect(tela, (100, 100, 100), [110, 100, 90, 40])

    tela.blit(sim, (30, 110))
    tela.blit(nao, (140, 110))

    pygame.display.update()
