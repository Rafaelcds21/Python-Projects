from datetime import datetime
ano_atual = datetime.now().year
for i in range(1, 8):
    ano_usuario = int(input('Insira o ano de nascimento: '))
    diferenca = ano_atual - ano_usuario
    if diferenca>18:
        print('Maioridade')
    else:
        print('Minoridade')
