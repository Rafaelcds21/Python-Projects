# Este é um programa feito para calcular o volume de sólidos. Qualquer dúvida ou sugestão é só comentar.

import numpy as np

# definir os volumes em funções


def piramide():
    a_base = float(input('Insira o valor da área da base: '))
    h = float(input('Insira o valor da altura: '))
    v_pir = a_base*h/3
    print(f'O valor do volume da pirâmide é: {v_pir}')


def cubo():
    l_quad = float(input('Insira o valor do lado do cubo: '))
    v_cubo = l_quad ** 3
    print(f'O valor do volume do cubo é: {v_cubo}')


def paralelepipedo():
    b = float(input('Insira o valor da base: '))
    l = float(input('Insira o valor da largura: '))
    h = float(input('Insira o valor da altura: '))
    v_para = b*l*h
    print(f'O valor do volume do paralelepípedo é: {v_para}')


def cilindro():
    r = float(input('Insira o valor do raio do cículo: '))
    h = float(input('Insira o valor da altura: '))
    a_cir = np.pi * (r ** 2)
    v_cil = a_cir*h
    print(f'O valor do volume do cilindro é: {v_cil}')


def esfera():
    r = float(input('Insira o valor do raio do cículo: '))
    v_esf = (4/3)*(np.pi*(r**3))
    print(f'O valor do volume da esfera é: {v_esf}')


# criar um método para chamar cada função individualmente
chama_volume = str(input('Insira o nome do poliedro: ')).lower()

if chama_volume == 'pirâmide' or 'piramide':
    piramide()

elif chama_volume == 'cubo':
    cubo()

elif chama_volume == 'paralelepípedo' or 'paralelepipedo':
    paralelepipedo()

elif chama_volume == 'cilidro':
    cilindro()

elif chama_volume == 'esfera':
    esfera()
