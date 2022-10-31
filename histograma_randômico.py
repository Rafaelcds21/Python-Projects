import random
import matplotlib.pyplot as plt

lista1 = []

for i in range(0, 101):
    lista1.append(i)

print(lista1)

lista2 = []

for i in range(1, 1001):
    lista2.append(random.choice(lista1))

print(lista2)

maior = 0
indice = 0
for i in range(0, 101):
    print(f'O número {i} apareceu {lista2.count(i)} vezes')
    if lista2.count(i) > maior:
        maior = lista2.count(i)
        indice = i

print(f'O número que apareceu mais vezes foi {indice}, com {maior} repetições')

plt.hist(lista2)
plt.show()
