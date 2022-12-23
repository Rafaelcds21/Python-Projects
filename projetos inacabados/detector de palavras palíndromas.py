frase = str(input('Qual palíndromo devo detectar? '))

lista = []

for i in range(0, len(frase)):
    lista.append(frase[i])

print(lista)

contador1 = 1

contador2 = 0

for i in range(0, len(lista)):
    if lista[i] == lista[i+len(lista)-contador1]:
        contador2 += 1

    contador1 += 2

if contador2 == len(lista)/2:
    print(f'{frase} é um palíndromo')
