numero = str(input('Insira um número entre 0 e 9999: '))
lista = []
for i in range(0, len(numero)):
    lista.append(numero[i])
print(f'Os algarismos do número são {lista}.')
