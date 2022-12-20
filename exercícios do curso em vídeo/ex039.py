from datetime import datetime
ano = int(input('Insira o ano de nascimento: '))
ano_prov_alis = datetime.now().year
diferenca = ano_prov_alis-ano
if diferenca < 18:
    print('Ainda é cedo.')
else:
    if diferenca == 18:
        print('Ano de alistamento.')
    else:
        print('Já passou do tempo de se alistar.')
