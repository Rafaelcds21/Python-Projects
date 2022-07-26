# Então pessoal, este arquivo serve para o cálculo de área de polígonos. Qualquer dúvida e sugestão é só comentar.

import numpy as np

# colocar cada área em funções próprias


def triangulo():
    b = float(input('Insira o valor da base do triângulo: '))
    h = float(input('Insira o valor da altura do triângulo: '))
    area_t = (b*h)/2
    print(f'O valor da área do triângulo é: {area_t}')


def quadrado():
    l_quad = float(input('Insira o valor do lado do quadrado: '))
    area_q = l_quad**2
    print(f'O valor da área do quadrado é: {area_q}')


def pentagono():
    l_pent = float(input('Insira o valor do lado do pentágono: '))
    a = float(input('Insira o valor do apótema do pentágono: '))
    area_p = 5*l_pent*a
    print(f'O valor da área do pentágono é: {area_p}')


def hexagono():
    l_hex = float(input('Insira o valor do lado do hexágono: '))
    area_h = (3*(l_hex**2)*(3**(1/2)))/2
    print(f'O valor da área do hexágono é: {area_h}')


def losango():
    D = float(input('Insira o valor da diagonal maior do losango: '))
    d = float(input('Insira o valor da diagonal menor do losango: '))
    a_los = (D*d)/2
    print(f'O valor da área do losango é: {a_los}')


def trapezio():
    B = float(input('Insira o valor da base maior do trapézio: '))
    b = float(input('Insira o valor da base menor do trapézio: '))
    h = float(input('Insira o valor da altura: '))
    a_trap = ((B+b)*h)/2
    print(f'O valor da área do trapézio é: {a_trap}')


def poligonoN():
    n = float(input('Insira o número de lados do polígono: '))
    ln = float(input('Insira o valor do lado do polígono: '))
    a = float(input('Insira o valor do apótema do polígono: '))
    a_nlados = (n*ln*a)/2
    print(f'O valor da área do polígono é: {a_nlados}')


def circulo():
    r = float(input('Insira o valor do raio do círculo: '))
    a_cir = np.pi*(r**2)
    print(f'O valor da área do círculo é: {a_cir}')


# criar um método para chamar uma função específica
chama_poligono = str(input('Digite o nome do polígono:')).lower()

if chama_poligono == 'triângulo' or 'triangulo':
    triangulo()

elif chama_poligono == 'quadrado':
    quadrado()

elif chama_poligono == 'pentagono':
    pentagono()

elif chama_poligono == 'hexágono' or 'hexagono':
    hexagono()

elif chama_poligono == 'losango':
    losango()

elif chama_poligono == 'trapézio' or 'trapezio':
    trapezio()

elif chama_poligono == 'outro':
    poligonoN()

elif chama_poligono == 'círculo' or 'circulo':
    circulo()
