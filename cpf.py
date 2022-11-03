import random

lista_algarismos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

input1 = input('Deseja inserir um cpf novo ou gerar um aleatoriamente? ').lower()

cpf_inicial = 0

if 'inserir' and 'manualmente' in input1:
    cpf1 = input('Insira os 9 primeiros digitos do cpf: ')
    cpf_inicial = cpf1

# elif 'aleatório' or 'aleatorio' or 'aleatoriamente' in input1:
    # cpf_aleatorio = random.sample(lista_algarismos, 9)
    # cpf_inicial = cpf_aleatorio

cpf_novo = cpf_inicial.replace('.', '')
print(cpf_novo)

lista = []

for i in range(0, len(cpf_novo)):
    lista.append(int(cpf_novo[i]))

print(lista)
