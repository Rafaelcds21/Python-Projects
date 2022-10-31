import random

lista = [['A Terra é redonda?', 'sim'], ['Em que ano o ser Humano pisou na Lua?', '1964'], ['Quanto é 1+1?', '2'], ['Como se diz "mesa" em inglês?', 'table'], ['Qual é a deriva de 1/x?', 'ln(x)']]

flag = True

while flag:
    pergunta_random = random.choice(lista)

    print(pergunta_random[0])

    resposta = str(input('Insira a resposta: '))

    if resposta == pergunta_random[1]:
        print('Parabéns, você acertou!')
    else:
        print('Precisa melhorar.')

    continuar = input('Deseja continuar? ').lower()

    if continuar == 'sim':
        flag = True
    else:
        flag = False
