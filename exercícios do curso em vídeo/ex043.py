peso = float(input('Insira o seu peso: '))
altura = float(input('Insira a sua altura: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Abaixo do peso.')

elif 18.5 < imc < 25:
    print('Peso ideal')

elif 25 < imc < 30:
    print('sobrepeso')

elif 30 < imc < 40:
    print('Obesidade')

else:
    print('Obesidade grave')
