from datetime import datetime

data = datetime.now()
ano_atual = data.year

ano_nascimento = int(input('Insira o ano de nascimento: '))

idade = ano_atual-ano_nascimento

if idade <= 9:
    print('MIRIM')

else:
    if 9 < idade <= 14:
        print('INFANTIL')

    else:
        if 14 < idade <= 19:
            print('JÚNIOR')

        else:
            if 19 < idade <= 25:
                print('SÊNIOR')

            else:
                print('IDOSO')
