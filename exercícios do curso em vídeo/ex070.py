menor = 99999999999999999999

cont_a = 0
cont_b = 0
cont_c = 0

lista_individual = []
lista_geral = []

while True:
    preco = int(input('Digite o preço do produto: '))
    nome = str(input('Digite o nome do produto: ')).lower()

    cont_a += preco

    if preco > 1000:
        cont_b += 1

    if preco < menor:
        menor = preco
        cont_c = nome

    lista_individual.append(preco)
    lista_individual.append(nome)

    lista_geral.append(lista_individual)

    continuar = str(input('Deseja continuar (sim ou não)? ')).lower()
    if continuar == 'sim':
        continue
    elif continuar == 'não' or 'nao':
        break

print(f'O total gasto foi {cont_a} reais. Existem {cont_b} produtos que custam mais de R$1000. O nome do produto mais '
      f'barato é {cont_c}.')

