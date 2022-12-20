valor_km = float(input('Insira o valor dos quilômetros rodados: '))
qtde_dias = int(input('Insira a quantidade de dias que o carro foi usado: '))
valor = (60*qtde_dias)+(0.15*valor_km)
print(f'Dado que o carro rodou um total de {valor_km} quilômetros e foi usado por {qtde_dias} dias, o valor total a '
      f'ser pago é R${valor:.2f}.')
