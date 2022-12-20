a = float(input('Insira o comprimento de uma reta: '))
b = float(input('Insira o comprimento de uma reta: '))
c = float(input('Insira o comprimento de uma reta: '))
if a < b + c:
    if b < a + c:
        if c < a + b:
            print('As retas podem formar um triângulo.')
        else:
            print('As retas não podem formar um triângulo.')
    else:
        print('As retas não podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
