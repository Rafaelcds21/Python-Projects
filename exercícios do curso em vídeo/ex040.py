n1 = float(input('Insira a 1° nota do aluno: '))
n2 = float(input('Insira a 2° nota do aluno: '))
media = (n1+n2)/2
if media >= 7.0:
    print('APROVADO')
else:
    if 5.0 <= media <= 6.9:
        print('RECUPERAÇÃO')
    else:
        print('REPROVADO')
