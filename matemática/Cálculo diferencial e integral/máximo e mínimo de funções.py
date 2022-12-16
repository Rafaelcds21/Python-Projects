from sympy import *


def funcao_2_grau(a, b, c):
    return a*(x**2)+b*x+c


# A 1° derivada determina os pontos críticos
# Se a 1° derivada for igual à 0 aquele ponto é um ponto crítico
x = Symbol('x')

A = float(input('Insira o valor de a: '))
B = float(input('Insira o valor de b: '))
C = float(input('Insira o valor de c: '))

expressao = funcao_2_grau(A, B, C)
print(expressao)


intervalo_x = input('Insira o intervalo entre colchetes "[]": ')

num1 = 0
num2 = 0

if intervalo_x[1] == '-':
    num_neg1 = -1*float(intervalo_x[2])
    num1 = num_neg1
    if intervalo_x[4] == '-':
        num_neg2 = -1*float(intervalo_x[5])
        num2 = num_neg2
    else:
        num2 = intervalo_x[4]
else:
    num1 = intervalo_x[1]
    num2 = intervalo_x[3]

tab1 = plot(expressao, (x, num1, num2), ylim=[-10, 10])
print(tab1)

eqdif = diff(expressao)
print(eqdif)

tab1 = plot(eqdif, (x, num1, num2), ylim=[-10, 10])
print(tab1)

contador = 0

for i in range(int(num1), int(num2)+1):
    if int(eqdif.subs(x, float(i))) == 0:
        # A 2° derivada determina o tipo de ponto crítico
        # 2° derivada < 0, ponto de mínimo
        # 2° derivada = 0, ponto de sela
        # 2° derivada > 0, ponto de máximo

        eqdif2 = diff(eqdif)
        print(eqdif2)

        if eqdif2.subs(x, float(i)) < 0:
            print(f'O valor {i} é ponto de máximo')
        elif eqdif2.subs(x, float(i)) == 0:
            print(f'O valor {i} é ponto de sela')
        else:
            print(f'O valor {i} é ponto de mínimo')
    else:
        contador += 1

if contador == int(num2)-int(num1)+1:
    print('Dentro do intervalo não foi encontrado nenhum número que seja ponto crítico')
