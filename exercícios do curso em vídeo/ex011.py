largura = float(input('Insira o valor da largura da parede: '))
altura = float(input('Insira o valor a altura da parede: '))
area = largura * altura
qtde_tinta = area/2
print(f'Dada a parede com uma largura de {largura} metros e uma altura de {altura} metros, a área é de {area} metros '
      f'quadrado e serão necessários {qtde_tinta} litros de tinta')
