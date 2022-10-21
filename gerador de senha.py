import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

inicio = input('Deseja gerar senha? ')

qtde_letras = int(input('Insira a quantidade de letras: '))
qtde_numeros = int(input('Insira a quantidade de números: '))

lista = []

if inicio == 'sim':
    if 0 < qtde_letras <= len(letras) and 0 < qtde_numeros <= len(numeros):
        letras_random = random.sample(letras, qtde_letras)
        numeros_random = random.sample(numeros, qtde_numeros)

        for i in range(0, len(letras_random)):
            lista.append(letras_random[i])

        for j in range(0, len(numeros_random)):
            lista.append(numeros_random[j])

        random.shuffle(lista)
        print(f'A sua senha é: {str(lista)}')

    else:
        print(f'Insira uma quantidade menor de números ou letras. Quantidade máxima de letras = {len(letras)}, quantidade máxima de números = {len(numeros)}')
