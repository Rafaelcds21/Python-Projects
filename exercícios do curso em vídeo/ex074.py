import random

maior = 0
menor = 99999999

num1 = random.randrange(0, 9)
num2 = random.randrange(0, 9)
num3 = random.randrange(0, 9)
num4 = random.randrange(0, 9)
num5 = random.randrange(0, 9)

tupla_numeros = (num1, num2, num3, num4, num5)

print(tupla_numeros)

for i in range(0, 5):
    print(tupla_numeros[i])

    if tupla_numeros[i] > maior:
        maior = tupla_numeros[i]

    if tupla_numeros[i] < menor:
        menor = tupla_numeros[i]

print(f"maior: {maior} ,menor: {menor}")
