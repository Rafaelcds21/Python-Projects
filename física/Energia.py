massa = float(input('Insira a massa (em kg): '))
velocidade = float(input('Insira a velocidade (em m/s): '))
energia_cinetica = (massa*velocidade**2)/2
print(f'{energia_cinetica} J')

massa = float(input('Insira a massa (em kg): '))
gravidade = 10.0
altura = float(input('Insira a altura (em m): '))
energia_potencial = massa * gravidade * altura
print(f'{energia_potencial} J')
