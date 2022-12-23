def massa_ideal(altura_real):
    massaidealmin = 18.5 * (altura_real ** 2)
    massaidealmax = 24.9 * (altura_real ** 2)
    return massaidealmin, massaidealmax


def altura_ideal(massa_real):
    alturaidealmin = (massa_real / 18.5) ** (1 / 2)
    alturaidealmax = (massa_real / 24.9) ** (1 / 2)
    return alturaidealmin, alturaidealmax


massa = float(input('Insira massa: '))
altura = float(input('Insira altura: '))

imc = massa/(altura**2)

print(imc)

massa_ideal_minima, massa_ideal_maxima = massa_ideal(altura)
altura_ideal_minima, altura_ideal_maxima = altura_ideal(massa)

if imc < 18.5:
    print(f"Você possui Magreza. Para a sua altura você deveria ter entre {massa_ideal_minima} e {massa_ideal_maxima} "
          f"e para o seu peso você deveria ter {altura_ideal_minima} e {altura_ideal_maxima}")

elif 18.5 < imc < 24.9:
    print("Você está com um peso ideal para sua altura.")

elif 25 < imc < 29.9:
    print(f"Você possui Sobrepeso. Para a sua altura você deveria ter entre {massa_ideal_minima} e "
          f"{massa_ideal_maxima} e para o seu peso você deveria ter {altura_ideal_minima} e {altura_ideal_maxima}")

elif 30 < imc < 34.9:
    print(f"Você possui Obesidade grau I. Para a sua altura você deveria ter entre {massa_ideal_minima} e "
          f"{massa_ideal_maxima} e para o seu peso você deveria ter {altura_ideal_minima} e {altura_ideal_maxima}")

elif 35 < imc < 39.9:
    print(f"Você possui Obesidade grau II. Para a sua altura você deveria ter entre {massa_ideal_minima} e "
          f"{massa_ideal_maxima} e para o seu peso você deveria ter {altura_ideal_minima} e {altura_ideal_maxima}")

elif imc > 40:
    print(f"Você possui Obesidade grau III. Para a sua altura você deveria ter entre {massa_ideal_minima} e "
          f"{massa_ideal_maxima} e para o seu peso você deveria ter {altura_ideal_minima} e {altura_ideal_maxima}")
