from random import choice
qtde_alunos = int(input('Insira a quantidade de alunos na sala: '))
lista = []
for i in range(1, qtde_alunos+1):
    nome = str(input('Insira o nome do aluno: '))
    lista.append(nome)
nome_sorteado = choice(lista)
print(f'O nome sorteado foi {nome_sorteado}.')

