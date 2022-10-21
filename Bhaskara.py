a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

if a != 0 and ((b**2) - 4*a*c)**(1/2) > 0:
    x1 = (-b + (((b**2) - 4*a*c)**(1/2))) / (2*a)
    x2 = (-b - (((b**2) - 4*a*c)**(1/2))) / (2*a)

    print(f'As raízes da equação ({a}) . x^2 + ({b}) . x + ({c}): {x1} e {x2}')
