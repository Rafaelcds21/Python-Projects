# Simulador da Mega Sena

import random

# Inserindo o intervalo de valores para o sorteio
num_min = int(input('Insira o menor número: '))
num_max = int(input('Insira o maior numero: '))

# Cria uma lista vazia para armazenar os numeros no intevalo entre o num_min e o num_max
lista = []

# Para cada valor i, indo de num_min até num_max+1 (a função for pega até o elemento anterior ao último valor, por
# isso o +1)
for i in range(num_min, num_max+1):
    lista.append(i)

# Pega uma amostra aleatória de 10 elementos da lista
numeros_sorteados = random.sample(lista, 10)

# Imprime no terminal
print(numeros_sorteados)
