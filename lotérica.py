from random import sample

lista = []

num_min = int(input('Insira o menor número da lista: '))
num_max = int(input('Insira o maior número da lista: '))

for i in range(num_min, num_max+1):
    lista.append(i)

qtde_amostra = int(input('Insira a quantidade de números a serem sorteados: '))

amostra = sample(lista, qtde_amostra)

print(amostra)
