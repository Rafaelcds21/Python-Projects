lista = []
for i in range(0, 3):
    numero = int(input('Insira um número: '))
    lista.append(numero)
lista = sorted(lista)
print(lista)
print(f'O maior é {lista[2]} e o menor é {lista[0]}')
