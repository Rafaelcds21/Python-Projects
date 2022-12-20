velocidade = str(input('Insira a velocidade do carro: '))
if velocidade[2] == ',':
    velocidade = velocidade.replace(',', '.')
velocidade = float(velocidade)
if velocidade > 80:
    diferenca = velocidade-80
    multa = 7.00*diferenca
    print(f'A multa foi de R${multa:.2f}')
else:
    print('O carro está dentro do limite.')
