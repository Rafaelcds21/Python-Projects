lista_geral = []
lista_velho = []
soma_idade = 0
contador = 0
velho = 0
contador_mulheres_jovens = 0

for i in range(1, 5):
    lista_individual = []

    nome = str(input('Insira o seu nome: '))
    idade = int(input('Insira a sua idade: '))
    sexo = str(input('Insira o seu sexo: '))

    lista_individual.append(nome)
    lista_individual.append(idade)
    lista_individual.append(sexo)

    lista_geral.append(lista_individual)

    soma_idade += idade
    contador += 1

for i in range(0, len(lista_geral)):
    if lista_geral[i][2] == 'M' or lista_geral[i][2] == 'm':
        if int(lista_geral[i][1]) > velho:
            lista_velho = lista_geral[i]

    elif lista_geral[i][2] == 'F' or lista_geral[i][2] == 'f':
        if lista_geral[i][1] < 20:
            contador_mulheres_jovens += 1

print(lista_geral)

media_idade = soma_idade/contador

print(media_idade)

print(lista_velho[0])

print(contador_mulheres_jovens)
