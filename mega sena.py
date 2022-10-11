import plotly.express as px
import pandas as pd

tabela = pd.read_excel('mega_sena_asloterias_ate_concurso_2527_sorteio.xlsx')
print(tabela)

bola1 = tabela['bola 1']
bola2 = tabela['bola 2']
bola3 = tabela['bola 3']
bola4 = tabela['bola 4']
bola5 = tabela['bola 5']
bola6 = tabela['bola 6']

lista = []

for i in range(0, 2527):
    lista.append(bola1[i])
    lista.append(bola2[i])
    lista.append(bola3[i])
    lista.append(bola4[i])
    lista.append(bola5[i])
    lista.append(bola6[i])

print(lista)

grafico = px.histogram(lista)
grafico.show()

grafico_bola1 = px.histogram(bola1)
grafico_bola1.show()

grafico_bola2 = px.histogram(bola2)
grafico_bola2.show()

grafico_bola3 = px.histogram(bola3)
grafico_bola3.show()

grafico_bola4 = px.histogram(bola4)
grafico_bola4.show()

grafico_bola5 = px.histogram(bola5)
grafico_bola5.show()

grafico_bola6 = px.histogram(bola6)
grafico_bola6.show()
