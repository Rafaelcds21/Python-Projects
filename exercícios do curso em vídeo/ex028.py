import random
num_min = int(input('Insira o menor número da lista: '))
num_max = int(input('Insira o maior numero da lista: '))
lista = []
for i in range(num_min, num_max):
    lista.append(i)
num_random = random.choice(lista)
num_user = int(input(f'Insira um número inteiro entre {num_min} e {num_max}: '))
if num_user == num_random:
    print(f'Parabéns, você ganhou do computador! Você escolheu {num_user} e o computador escolheu {num_random}.')
else:
    print(f'Tente novamente, a máguina venceu. Você escolheu {num_user} e o computador escolheu {num_random}.')
