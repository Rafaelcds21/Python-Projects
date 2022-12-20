nome = str(input('Insira um nome: '))
nomes_separados = nome.split(' ')
contador = -1
for i in range(0, len(nomes_separados)):
    contador += 1
print(contador)
print(f'O 1° nome é {nomes_separados[0]} e o último nome é {nomes_separados[contador]}')
