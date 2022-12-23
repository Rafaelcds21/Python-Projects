import pygame
from pygame.locals import *
from sys import exit
from cenário import casainterior, ceu, chao
from player import players
from itens import itens
from inimigos import inimigos


def avanco_goblin_guerreiro():
    pygame.init()

    tela = pygame.display.set_mode((512, 320))

    while True:
        tela.fill((0, 0, 0))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 256 and 60 <= mouse[1] <= 100:
                    players.goblin_guerreiro.rect.x = 0

                    players.goblin_guerreiro.rect.y = 192

                    while True:
                        tela.fill((0, 0, 0))

                        mouse = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                exit()

                            if event.type == KEYDOWN:
                                if event.key == K_a:
                                    players.goblin_guerreiro.rect.x -= 10
                                if event.key == K_d:
                                    players.goblin_guerreiro.rect.x += 10
                                if event.key == K_w:
                                    players.goblin_guerreiro.rect.y -= 10
                                if event.key == K_s:
                                    players.goblin_guerreiro.rect.y += 10

                        if players.goblin_guerreiro.rect.x == 20 and players.goblin_guerreiro.rect.y == 192:
                            while True:
                                tela.fill((0, 0, 0))

                                mouse = pygame.mouse.get_pos()

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        exit()

                                    if event.type == KEYDOWN:
                                        if event.key == K_a:
                                            players.goblin_guerreiro.rect.x -= 10
                                        if event.key == K_d:
                                            players.goblin_guerreiro.rect.x += 10
                                        if event.key == K_w:
                                            players.goblin_guerreiro.rect.y -= 10
                                        if event.key == K_s:
                                            players.goblin_guerreiro.rect.y += 10

                                casainterior.lista.draw(tela)
                                casainterior.lista.update()

                                itens.lista_bau_fechado.draw(tela)
                                itens.lista_bau_fechado.update()

                                inimigos.lista_gosmas_minions.draw(tela)
                                inimigos.lista_gosmas_minions.update()

                                players.lista_goblin_guerreiro.draw(tela)
                                players.lista_goblin_guerreiro.update()

                                pygame.display.update()

                        ceu.lista_mapa.draw(tela)
                        ceu.lista_mapa.update()

                        chao.lista_mapa.draw(tela)
                        chao.lista_mapa.update()

                        players.lista_goblin_guerreiro.draw(tela)
                        players.lista_goblin_guerreiro.update()

                        pygame.display.update()


def avanco_humano_guerreiro():
    pygame.init()

    tela = pygame.display.set_mode((512, 320))

    while True:
        tela.fill((0, 0, 0))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 256 and 60 <= mouse[1] <= 100:
                    players.feiticeiro.rect.x = 0

                    players.feiticeiro.rect.y = 192

                    while True:
                        tela.fill((0, 0, 0))

                        mouse = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                exit()

                            if event.type == KEYDOWN:
                                if event.key == K_a:
                                    players.humano_guerreiro.rect.x -= 10
                                if event.key == K_d:
                                    players.humano_guerreiro.rect.x += 10
                                if event.key == K_w:
                                    players.humano_guerreiro.rect.y -= 10
                                if event.key == K_s:
                                    players.humano_guerreiro.rect.y += 10

                        if players.feiticeiro.rect.x == 20 and players.feiticeiro.rect.y == 192:
                            while True:
                                tela.fill((0, 0, 0))

                                mouse = pygame.mouse.get_pos()

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        exit()

                                    if event.type == KEYDOWN:
                                        if event.key == K_a:
                                            players.humano_guerreiro.rect.x -= 10
                                        if event.key == K_d:
                                            players.humano_guerreiro.rect.x += 10
                                        if event.key == K_w:
                                            players.humano_guerreiro.rect.y -= 10
                                        if event.key == K_s:
                                            players.humano_guerreiro.rect.y += 10

                                casainterior.lista.draw(tela)
                                casainterior.lista.update()

                                itens.lista_bau_fechado.draw(tela)
                                itens.lista_bau_fechado.update()

                                inimigos.lista_gosmas_minions.draw(tela)
                                inimigos.lista_gosmas_minions.update()

                                players.lista_humano_guerreiro.draw(tela)
                                players.lista_humano_guerreiro.update()

                                pygame.display.update()

                        ceu.lista_mapa.draw(tela)
                        ceu.lista_mapa.update()

                        chao.lista_mapa.draw(tela)
                        chao.lista_mapa.update()

                        players.lista_humano_guerreiro.draw(tela)
                        players.lista_humano_guerreiro.update()

                        pygame.display.update()


def avanco_meio_orc_guerreiro():
    pygame.init()

    tela = pygame.display.set_mode((512, 320))

    while True:
        tela.fill((0, 0, 0))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 256 and 60 <= mouse[1] <= 100:
                    players.feiticeiro.rect.x = 0

                    players.feiticeiro.rect.y = 192

                    while True:
                        tela.fill((0, 0, 0))

                        mouse = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                exit()

                            if event.type == KEYDOWN:
                                if event.key == K_a:
                                    players.meio_orc_guerreiro.rect.x -= 10
                                if event.key == K_d:
                                    players.meio_orc_guerreiro.rect.x += 10
                                if event.key == K_w:
                                    players.meio_orc_guerreiro.rect.y -= 10
                                if event.key == K_s:
                                    players.meio_orc_guerreiro.rect.y += 10

                        if players.feiticeiro.rect.x == 20 and players.feiticeiro.rect.y == 192:
                            while True:
                                tela.fill((0, 0, 0))

                                mouse = pygame.mouse.get_pos()

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        exit()

                                    if event.type == KEYDOWN:
                                        if event.key == K_a:
                                            players.meio_orc_guerreiro.rect.x -= 10
                                        if event.key == K_d:
                                            players.meio_orc_guerreiro.rect.x += 10
                                        if event.key == K_w:
                                            players.meio_orc_guerreiro.rect.y -= 10
                                        if event.key == K_s:
                                            players.meio_orc_guerreiro.rect.y += 10

                                casainterior.lista.draw(tela)
                                casainterior.lista.update()

                                itens.lista_bau_fechado.draw(tela)
                                itens.lista_bau_fechado.update()

                                inimigos.lista_gosmas_minions.draw(tela)
                                inimigos.lista_gosmas_minions.update()

                                players.lista_meio_orc_guerreiro.draw(tela)
                                players.lista_meio_orc_guerreiro.update()

                                pygame.display.update()

                        ceu.lista_mapa.draw(tela)
                        ceu.lista_mapa.update()

                        chao.lista_mapa.draw(tela)
                        chao.lista_mapa.update()

                        players.lista_meio_orc_guerreiro.draw(tela)
                        players.lista_meio_orc_guerreiro.update()

                        pygame.display.update()


def avanco_elfo_guerreiro():
    pygame.init()

    tela = pygame.display.set_mode((512, 320))

    while True:
        tela.fill((0, 0, 0))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 256 and 60 <= mouse[1] <= 100:
                    players.elfo_guerreiro.rect.x = 0

                    players.elfo_guerreiro.rect.y = 192

                    while True:
                        tela.fill((0, 0, 0))

                        mouse = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                exit()

                            if event.type == KEYDOWN:
                                if event.key == K_a:
                                    players.elfo_guerreiro.rect.x -= 10
                                if event.key == K_d:
                                    players.elfo_guerreiro.rect.x += 10
                                if event.key == K_w:
                                    players.elfo_guerreiro.rect.y -= 10
                                if event.key == K_s:
                                    players.elfo_guerreiro.rect.y += 10

                        if players.elfo_guerreiro.rect.x == 20 and players.elfo_guerreiro.rect.y == 192:
                            while True:
                                tela.fill((0, 0, 0))

                                mouse = pygame.mouse.get_pos()

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        exit()

                                    if event.type == KEYDOWN:
                                        if event.key == K_a:
                                            players.elfo_guerreiro.rect.x -= 10
                                        if event.key == K_d:
                                            players.elfo_guerreiro.rect.x += 10
                                        if event.key == K_w:
                                            players.elfo_guerreiro.rect.y -= 10
                                        if event.key == K_s:
                                            players.elfo_guerreiro.rect.y += 10

                                casainterior.lista.draw(tela)
                                casainterior.lista.update()

                                itens.lista_bau_fechado.draw(tela)
                                itens.lista_bau_fechado.update()

                                inimigos.lista_gosmas_minions.draw(tela)
                                inimigos.lista_gosmas_minions.update()

                                players.lista_elfo_guerreiro.draw(tela)
                                players.lista_elfo_guerreiro.update()

                                pygame.display.update()

                        ceu.lista_mapa.draw(tela)
                        ceu.lista_mapa.update()

                        chao.lista_mapa.draw(tela)
                        chao.lista_mapa.update()

                        players.lista_elfo_guerreiro.draw(tela)
                        players.lista_elfo_guerreiro.update()

                        pygame.display.update()


def avanco_arqueiro():
    pygame.init()

    tela = pygame.display.set_mode((512, 320))

    while True:
        tela.fill((0, 0, 0))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 256 and 60 <= mouse[1] <= 100:
                    players.arqueiro.rect.x = 0

                    players.arqueiro.rect.y = 192

                    while True:
                        tela.fill((0, 0, 0))

                        mouse = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                exit()

                            if event.type == KEYDOWN:
                                if event.key == K_a:
                                    players.arqueiro.rect.x -= 10
                                if event.key == K_d:
                                    players.arqueiro.rect.x += 10
                                if event.key == K_w:
                                    players.arqueiro.rect.y -= 10
                                if event.key == K_s:
                                    players.arqueiro.rect.y += 10

                        if players.feiticeiro.rect.x == 20 and players.feiticeiro.rect.y == 192:
                            while True:
                                tela.fill((0, 0, 0))

                                mouse = pygame.mouse.get_pos()

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        exit()

                                    if event.type == KEYDOWN:
                                        if event.key == K_a:
                                            players.arqueiro.rect.x -= 10
                                        if event.key == K_d:
                                            players.arqueiro.rect.x += 10
                                        if event.key == K_w:
                                            players.arqueiro.rect.y -= 10
                                        if event.key == K_s:
                                            players.arqueiro.rect.y += 10

                                casainterior.lista.draw(tela)
                                casainterior.lista.update()

                                itens.lista_bau_fechado.draw(tela)
                                itens.lista_bau_fechado.update()

                                inimigos.lista_gosmas_minions.draw(tela)
                                inimigos.lista_gosmas_minions.update()

                                players.lista_arqueiro.draw(tela)
                                players.lista_arqueiro.update()

                                pygame.display.update()

                        ceu.lista_mapa.draw(tela)
                        ceu.lista_mapa.update()

                        chao.lista_mapa.draw(tela)
                        chao.lista_mapa.update()

                        players.lista_arqueiro.draw(tela)
                        players.lista_arqueiro.update()

                        pygame.display.update()


def avanco_paladino():
    pygame.init()

    tela = pygame.display.set_mode((512, 320))

    while True:
        tela.fill((0, 0, 0))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 256 and 60 <= mouse[1] <= 100:
                    players.paladino.rect.x = 0

                    players.paladino.rect.y = 192

                    while True:
                        tela.fill((0, 0, 0))

                        mouse = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                exit()

                            if event.type == KEYDOWN:
                                if event.key == K_a:
                                    players.paladino.rect.x -= 10
                                if event.key == K_d:
                                    players.paladino.rect.x += 10
                                if event.key == K_w:
                                    players.paladino.rect.y -= 10
                                if event.key == K_s:
                                    players.paladino.rect.y += 10

                        if players.paladino.rect.x == 20 and players.paladino.rect.y == 192:
                            while True:
                                tela.fill((0, 0, 0))

                                mouse = pygame.mouse.get_pos()

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        exit()

                                    if event.type == KEYDOWN:
                                        if event.key == K_a:
                                            players.paladino.rect.x -= 10
                                        if event.key == K_d:
                                            players.paladino.rect.x += 10
                                        if event.key == K_w:
                                            players.paladino.rect.y -= 10
                                        if event.key == K_s:
                                            players.paladino.rect.y += 10

                                casainterior.lista.draw(tela)
                                casainterior.lista.update()

                                itens.lista_bau_fechado.draw(tela)
                                itens.lista_bau_fechado.update()

                                inimigos.lista_gosmas_minions.draw(tela)
                                inimigos.lista_gosmas_minions.update()

                                players.lista_paladino.draw(tela)
                                players.lista_paladino.update()

                                pygame.display.update()

                        ceu.lista_mapa.draw(tela)
                        ceu.lista_mapa.update()

                        chao.lista_mapa.draw(tela)
                        chao.lista_mapa.update()

                        players.lista_paladino.draw(tela)
                        players.lista_paladino.update()

                        pygame.display.update()


def avanco_mago():
    pygame.init()

    tela = pygame.display.set_mode((512, 320))

    while True:
        tela.fill((0, 0, 0))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 256 and 60 <= mouse[1] <= 100:
                    players.mago.rect.x = 0

                    players.mago.rect.y = 192

                    while True:
                        tela.fill((0, 0, 0))

                        mouse = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                exit()

                            if event.type == KEYDOWN:
                                if event.key == K_a:
                                    players.mago.rect.x -= 10
                                if event.key == K_d:
                                    players.mago.rect.x += 10
                                if event.key == K_w:
                                    players.mago.rect.y -= 10
                                if event.key == K_s:
                                    players.mago.rect.y += 10

                        if players.mago.rect.x == 20 and players.mago.rect.y == 192:
                            while True:
                                tela.fill((0, 0, 0))

                                mouse = pygame.mouse.get_pos()

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        exit()

                                    if event.type == KEYDOWN:
                                        if event.key == K_a:
                                            players.mago.rect.x -= 10
                                        if event.key == K_d:
                                            players.mago.rect.x += 10
                                        if event.key == K_w:
                                            players.mago.rect.y -= 10
                                        if event.key == K_s:
                                            players.mago.rect.y += 10

                                casainterior.lista.draw(tela)
                                casainterior.lista.update()

                                itens.lista_bau_fechado.draw(tela)
                                itens.lista_bau_fechado.update()

                                inimigos.lista_gosmas_minions.draw(tela)
                                inimigos.lista_gosmas_minions.update()

                                players.lista_mago.draw(tela)
                                players.lista_mago.update()

                                pygame.display.update()

                        ceu.lista_mapa.draw(tela)
                        ceu.lista_mapa.update()

                        chao.lista_mapa.draw(tela)
                        chao.lista_mapa.update()

                        players.lista_mago.draw(tela)
                        players.lista_mago.update()

                        pygame.display.update()


def avanco_feiticeiro():
    pygame.init()

    tela = pygame.display.set_mode((512, 320))

    while True:
        tela.fill((0, 0, 0))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 256 and 60 <= mouse[1] <= 100:
                    players.feiticeiro.rect.x = 0

                    players.feiticeiro.rect.y = 192

                    while True:
                        tela.fill((0, 0, 0))

                        mouse = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                exit()

                            if event.type == KEYDOWN:
                                if event.key == K_a:
                                    players.feiticeiro.rect.x -= 10
                                if event.key == K_d:
                                    players.feiticeiro.rect.x += 10
                                if event.key == K_w:
                                    players.feiticeiro.rect.y -= 10
                                if event.key == K_s:
                                    players.feiticeiro.rect.y += 10

                        if players.feiticeiro.rect.x == 20 and players.feiticeiro.rect.y == 192:
                            while True:
                                tela.fill((0, 0, 0))

                                mouse = pygame.mouse.get_pos()

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        exit()

                                    if event.type == KEYDOWN:
                                        if event.key == K_a:
                                            players.feiticeiro.rect.x -= 10
                                        if event.key == K_d:
                                            players.feiticeiro.rect.x += 10
                                        if event.key == K_w:
                                            players.feiticeiro.rect.y -= 10
                                        if event.key == K_s:
                                            players.feiticeiro.rect.y += 10

                                casainterior.lista.draw(tela)
                                casainterior.lista.update()

                                itens.lista_bau_fechado.draw(tela)
                                itens.lista_bau_fechado.update()

                                inimigos.lista_gosmas_minions.draw(tela)
                                inimigos.lista_gosmas_minions.update()

                                players.lista_feiticeiro.draw(tela)
                                players.lista_feiticeiro.update()

                                pygame.display.update()

                        ceu.lista_mapa.draw(tela)
                        ceu.lista_mapa.update()

                        chao.lista_mapa.draw(tela)
                        chao.lista_mapa.update()

                        players.lista_feiticeiro.draw(tela)
                        players.lista_feiticeiro.update()


                        pygame.display.update()
