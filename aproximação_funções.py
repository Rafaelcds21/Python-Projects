from random import *

x = 0

# Insere a função
func = str(input('Insira a função: ')).lower().strip()

# Se a função for quadrática, cria-se uma função interna no python que será usada a seguir.
if ('x²' or 'x^2' or 'x**2' in func) and ('-' not in func):
    func = func.split('+')

    if '.' in func[0]:
        a = func[0].split('.')[0]
    else:
        a = func[0].split('x')[0]

        if a == '':
            a = 1

    if len(func) >= 2:
        if '.' in func[1]:
            b = func[1].split('.')[1]
        else:
            b = func[1].split('x')[0]

            if b == '':
                b = 1
    elif len(func) < 2:
        b = 0

    if len(func) == 3:
        c = func[2]
    elif len(func) < 3:
        c = 0

    a = float(a)
    b = float(b)
    c = float(c)

    def funcao(x, a, b, c):
        return (a*(x**2)) + (b*x) + c

# Aqui será inserido o target, o valor de y que determinará o valor de x a ser "adivinhado"
y = int(input("Insira o target: "))

'''
Aqui será onde "chutaremos" o valor de x, onde f(x)=y

A questão que eu preciso codificar é qual vai ser a margem de diferença do valor exato que eu preciso atingir para que o
intervalo seja cortado pela metade.

Com a biblioteca random importada na linha 1, é possível selecionar 1 valor dentro de uma lista com a função sample
'''
intevalo = [-10, 10]

x1, x2 = 0, 1

for i in range(0, 1000):
    valores = sample(intevalo, 2)

    x1, x2 = valores[0], valores[1]

    if (funcao(x1, a, b, c) < y < funcao(x2, a, b, c)) or (funcao(x2, a, b, c) < y < funcao(x1, a, b, c)):
        break

while abs(x1-x2) > 0.01:
    x3 = (x1 + x2)/2
    if (funcao(x1, a, b, c) - y) * (funcao(x3, a, b, c) - y) > 0:
        x1 = x3
    else:
        x2 = x3

print(f"A solução aproximada está no intevalo [{x1},{x2}]")
