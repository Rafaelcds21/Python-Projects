from random import choice
qtde_alunos = int(input('Insira a quantidade de alunos na sala: '))
lista = []
for i in range(1, qtde_alunos+1):
    nome = str(input('Insira o nome do aluno: '))
    lista.append(nome)
qtde_apresentacoes = int(input('Insira o número de alunos que irão apresentar: '))
for i in range(1, qtde_apresentacoes+1):
    nome_sorteado = choice(lista)
    print(f'O {i}° nome sorteado foi {nome_sorteado}.')
    lista.remove(nome_sorteado)

