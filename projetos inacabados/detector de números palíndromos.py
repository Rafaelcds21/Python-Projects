qtde_zeros = int(input('Insira a quantidade de caracteres: '))

num_palindromo = int(input('Insira um número: '))

# milhar = num_palindromo//1000
# centena = (num_palindromo-1000*milhar)//100
# dezena = (num_palindromo-100*centena-1000*milhar)//10
# unidade = num_palindromo-10*dezena-100*centena-1000*milhar

# print(milhar)
# print(centena)
# print(dezena)
# print(unidade)

# if milhar == unidade and centena == dezena:
    # print(f'O número {num_palindromo} é um palíndromo.')
# else:
    # print(f'O número {num_palindromo} não é um palíndromo')

for i in range(qtde_zeros+1, 1, -1):
    caracter = num_palindromo//(10**i)
    caracter2 = num_palindromo - (10**i) * caracter
    print(caracter)
    print(caracter2)
