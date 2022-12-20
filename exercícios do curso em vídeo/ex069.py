cont_a = 0
cont_b = 0
cont_c = 0

lista_pessoal = []
lista_geral = []

while True:
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Digite um sexo (m ou f): ')).lower()

    if idade > 18:
        cont_a += 1
    if sexo == 'm':
        cont_b += 1
    if sexo == 'f' and idade < 20:
        cont_c += 1

    lista_pessoal.append(idade)
    lista_pessoal.append(sexo)

    lista_geral.append(lista_pessoal)

    continuar = str(input('Deseja continuar (sim ou não)? ')).lower()
    if continuar == 'sim':
        continue
    elif continuar == 'não' or 'nao':
        break

print(f'Existem {cont_a} pessoas com mais de 18 anos. Existem {cont_b} homens. Existem {cont_c} mulheres com menos de '
      f'20 anos.')

