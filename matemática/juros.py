vi = float(input("Insira o valor inicial do investimento: "))

juros = float(input("Insira os juros sobre o valor do investimento (em notação decimal): "))

tempo = int(input("Insira o tempo do investimento (em meses): "))

for i in range(1, tempo+1):
    vi = (1+juros) * vi
    print(f'{i}° prestação: {vi:.2f}')
