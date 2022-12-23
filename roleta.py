import random

print('='*20)
print('Bem-vindo a roleta')
print('='*20)
nome = str(input('Qual o seu nome? '))
print(f'Bem-vindo, {nome}')
print('Digite "sair" para sair da mesa.')

flag = True

aposta = str(input('Insira sua aposta: ')).lower()

lista_cor = ['vermelho', 'preto']

lista_numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                 '19', '20', '21']

cor_escolhida = random.choice(lista_cor)
numero_escolhido = random.choice(lista_numeros)

contador_vitorias = 0
contador_derrotas = 0

while flag:
    if aposta != 'sair':
        if len(aposta.split(' ')) == 2:
            if aposta == f'{numero_escolhido} {cor_escolhida}':
                print(f'Você ganhou! O número sorteado foi {numero_escolhido} {cor_escolhida}')
                contador_vitorias += 1
            else:
                print(f'Você perdeu! O número sorteado foi {numero_escolhido} {cor_escolhida}')
                contador_derrotas += 1

        else:
            cor_escolhida2 = random.choice(lista_cor)
            if aposta == cor_escolhida2:
                print(f'Você ganhou! A cor sorteada foi {cor_escolhida2}')
                contador_vitorias += 1
            else:
                print(f'Você perdeu! A cor sorteada foi {cor_escolhida2}')
                contador_derrotas += 1

        aposta = str(input('Insira sua aposta: ')).lower()

        cor_escolhida = random.choice(lista_cor)
        numero_escolhido = random.choice(lista_numeros)

    else:
        flag = False

print(f'Obrigado por jogar, você ganhou {contador_vitorias} vezes e perdeu {contador_derrotas} vezes.')
