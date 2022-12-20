valor_km = float(input('Insira o valor da distância da viagem: '))
if valor_km <= 200.0:
    valor_viagem = 0.50 * valor_km
    print(f'O valor da viagem é R${valor_viagem:.2f}.')
else:
    valor_viagem = 0.45 * valor_km
    print(f'O valor da viagem é R${valor_viagem:.2f}.')
