import pygame
from pygame.locals import *
from sys import exit

pygame.init()


def fichagoblinguerreiro():
    fonte = pygame.font.Font('freesansbold.ttf', 16)
    texto1 = fonte.render('Ficha Goblin guerreiro', True, (0, 255, 0))
    texto2 = fonte.render('Força: ', True, (0, 255, 0))
    texto3 = fonte.render('Destreza: ', True, (0, 255, 0))
    texto4 = fonte.render('Constituição: ', True, (0, 255, 0))
    texto5 = fonte.render('Inteligência: ', True, (0, 255, 0))
    texto6 = fonte.render('Sabedoria: ', True, (0, 255, 0))
    texto7 = fonte.render('Carisma: ', True, (0, 255, 0))
    tela.blit(texto1, (0, 80))
    tela.blit(texto2, (0, 100))
    tela.blit(texto3, (0, 120))
    tela.blit(texto4, (0, 140))
    tela.blit(texto5, (0, 160))
    tela.blit(texto6, (0, 180))
    tela.blit(texto7, (0, 200))


def fichahumanoguerreiro():
    fonte = pygame.font.Font('freesansbold.ttf', 16)
    texto1 = fonte.render('Ficha Humano guerreiro', True, (0, 255, 0))
    texto2 = fonte.render('Força: ', True, (0, 255, 0))
    texto3 = fonte.render('Destreza: ', True, (0, 255, 0))
    texto4 = fonte.render('Constituição: ', True, (0, 255, 0))
    texto5 = fonte.render('Inteligência: ', True, (0, 255, 0))
    texto6 = fonte.render('Sabedoria: ', True, (0, 255, 0))
    texto7 = fonte.render('Carisma: ', True, (0, 255, 0))
    tela.blit(texto1, (0, 80))
    tela.blit(texto2, (0, 100))
    tela.blit(texto3, (0, 120))
    tela.blit(texto4, (0, 140))
    tela.blit(texto5, (0, 160))
    tela.blit(texto6, (0, 180))
    tela.blit(texto7, (0, 200))


def fichameioorcguerreiro():
    fonte = pygame.font.Font('freesansbold.ttf', 16)
    texto1 = fonte.render('Ficha Meio Orc guerreiro', True, (0, 255, 0))
    texto2 = fonte.render('Força: ', True, (0, 255, 0))
    texto3 = fonte.render('Destreza: ', True, (0, 255, 0))
    texto4 = fonte.render('Constituição: ', True, (0, 255, 0))
    texto5 = fonte.render('Inteligência: ', True, (0, 255, 0))
    texto6 = fonte.render('Sabedoria: ', True, (0, 255, 0))
    texto7 = fonte.render('Carisma: ', True, (0, 255, 0))
    tela.blit(texto1, (0, 80))
    tela.blit(texto2, (0, 100))
    tela.blit(texto3, (0, 120))
    tela.blit(texto4, (0, 140))
    tela.blit(texto5, (0, 160))
    tela.blit(texto6, (0, 180))
    tela.blit(texto7, (0, 200))


def fichaelfoguerreiro():
    fonte = pygame.font.Font('freesansbold.ttf', 16)
    texto1 = fonte.render('Ficha Elfo guerreiro', True, (0, 255, 0))
    texto2 = fonte.render('Força: ', True, (0, 255, 0))
    texto3 = fonte.render('Destreza: ', True, (0, 255, 0))
    texto4 = fonte.render('Constituição: ', True, (0, 255, 0))
    texto5 = fonte.render('Inteligência: ', True, (0, 255, 0))
    texto6 = fonte.render('Sabedoria: ', True, (0, 255, 0))
    texto7 = fonte.render('Carisma: ', True, (0, 255, 0))
    tela.blit(texto1, (0, 80))
    tela.blit(texto2, (0, 100))
    tela.blit(texto3, (0, 120))
    tela.blit(texto4, (0, 140))
    tela.blit(texto5, (0, 160))
    tela.blit(texto6, (0, 180))
    tela.blit(texto7, (0, 200))


def fichaarqueiro():
    fonte = pygame.font.Font('freesansbold.ttf', 16)
    texto1 = fonte.render('Ficha Arqueiro', True, (0, 255, 0))
    texto2 = fonte.render('Força: 13', True, (0, 255, 0))
    texto3 = fonte.render('Destreza: 15', True, (0, 255, 0))
    texto4 = fonte.render('Constituição: 14', True, (0, 255, 0))
    texto5 = fonte.render('Inteligência: 8', True, (0, 255, 0))
    texto6 = fonte.render('Sabedoria: 10', True, (0, 255, 0))
    texto7 = fonte.render('Carisma: 12', True, (0, 255, 0))
    tela.blit(texto1, (0, 80))
    tela.blit(texto2, (0, 100))
    tela.blit(texto3, (0, 120))
    tela.blit(texto4, (0, 140))
    tela.blit(texto5, (0, 160))
    tela.blit(texto6, (0, 180))
    tela.blit(texto7, (0, 200))


def fichapaladino():
    fonte = pygame.font.Font('freesansbold.ttf', 16)
    texto1 = fonte.render('Ficha Paladino', True, (0, 255, 0))
    texto2 = fonte.render('Força: 15', True, (0, 255, 0))
    texto3 = fonte.render('Destreza: 13', True, (0, 255, 0))
    texto4 = fonte.render('Constituição: 14', True, (0, 255, 0))
    texto5 = fonte.render('Inteligência: 8', True, (0, 255, 0))
    texto6 = fonte.render('Sabedoria: 10', True, (0, 255, 0))
    texto7 = fonte.render('Carisma: 12', True, (0, 255, 0))
    tela.blit(texto1, (0, 80))
    tela.blit(texto2, (0, 100))
    tela.blit(texto3, (0, 120))
    tela.blit(texto4, (0, 140))
    tela.blit(texto5, (0, 160))
    tela.blit(texto6, (0, 180))
    tela.blit(texto7, (0, 200))


def fichamago():
    fonte = pygame.font.Font('freesansbold.ttf', 16)
    texto1 = fonte.render('Ficha Mago', True, (0, 255, 0))
    texto2 = fonte.render('Força: 8', True, (0, 255, 0))
    texto3 = fonte.render('Destreza: 13', True, (0, 255, 0))
    texto4 = fonte.render('Constituição: 14', True, (0, 255, 0))
    texto5 = fonte.render('Inteligência: 15', True, (0, 255, 0))
    texto6 = fonte.render('Sabedoria: 12', True, (0, 255, 0))
    texto7 = fonte.render('Carisma: 10', True, (0, 255, 0))
    tela.blit(texto1, (0, 80))
    tela.blit(texto2, (0, 100))
    tela.blit(texto3, (0, 120))
    tela.blit(texto4, (0, 140))
    tela.blit(texto5, (0, 160))
    tela.blit(texto6, (0, 180))
    tela.blit(texto7, (0, 200))


def fichafeiticeiro():
    fonte = pygame.font.Font('freesansbold.ttf', 16)
    texto1 = fonte.render('Ficha Feiticeiro', True, (0, 255, 0))
    texto2 = fonte.render('Força: 8', True, (0, 255, 0))
    texto3 = fonte.render('Destreza: 12', True, (0, 255, 0))
    texto4 = fonte.render('Constituição: 13', True, (0, 255, 0))
    texto5 = fonte.render('Inteligência: 10', True, (0, 255, 0))
    texto6 = fonte.render('Sabedoria: 15', True, (0, 255, 0))
    texto7 = fonte.render('Carisma: 14', True, (0, 255, 0))
    tela.blit(texto1, (0, 80))
    tela.blit(texto2, (0, 100))
    tela.blit(texto3, (0, 120))
    tela.blit(texto4, (0, 140))
    tela.blit(texto5, (0, 160))
    tela.blit(texto6, (0, 180))
    tela.blit(texto7, (0, 200))


tela = pygame.display.set_mode((500, 500))
