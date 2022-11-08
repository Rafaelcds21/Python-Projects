import requests
import json
from tkinter import *
import datetime

data = datetime.datetime.now()
dia = data.day

requisicao = requests.get('https://api.hgbrasil.com/weather?woeid=455825')
conteudo = json.loads(requisicao.content)
print(conteudo)

# hoje
json = conteudo['results']
temperatura = conteudo['results']['temp']
data = conteudo['results']['date']
tempo = conteudo['results']['time']
codigo_condicao = conteudo['results']['condition_code']
descricao = conteudo['results']['description']
currently = conteudo['results']['currently']
cid = conteudo['results']['cid']
cidade = conteudo['results']['city']
img = conteudo['results']['img_id']
umidade = conteudo['results']['humidity']
cloudiness = conteudo['results']['cloudiness']
chuva = conteudo['results']['rain']
velocidade_do_vento = conteudo['results']['wind_speedy']
direcao_do_vento = conteudo['results']['wind_direction']
nascer_do_sol = conteudo['results']['sunrise']
por_do_sol = conteudo['results']['sunset']
condition_slug = conteudo['results']['condition_slug']
nome_cidade = conteudo['results']['city_name']

janela = Tk()

janela.title("Clima")
janela.geometry("300x300")

texto = Label(janela, text="Clique no botão para ver o clima do dia de hoje")
texto.grid(column=0, row=0, padx=10, pady=10)


def dia_1(event):
    texto_resposta_1 = Label(janela, text=f"dia: {conteudo['results']['forecast'][1]['date']}/2022\n"
                                          f"weekday: {conteudo['results']['forecast'][1]['weekday']}\n"
                                          f"temp_max: {conteudo['results']['forecast'][1]['max']}°C\n"
                                          f"temp_min: {conteudo['results']['forecast'][1]['min']}°C\n"
                                          f"cloudiness: {conteudo['results']['forecast'][1]['cloudiness']}\n"
                                          f"rain: {conteudo['results']['forecast'][1]['rain']} mm\n"
                                          f"rain_probability: {conteudo['results']['forecast'][1]['rain_probability']}%\n"
                                          f"windy_speedy: {conteudo['results']['forecast'][1]['wind_speedy']}\n"
                                          f"description: {conteudo['results']['forecast'][1]['description']}\n"
                                          f"condição: {conteudo['results']['forecast'][1]['condition']}")
    texto_resposta_1.grid(column=5, row=2, padx=10, pady=5)
    return texto_resposta_1


def dia_2(event):
    texto_resposta_1 = Label(janela, text=f"dia: {conteudo['results']['forecast'][2]['date']}/2022\n"
                                          f"weekday: {conteudo['results']['forecast'][2]['weekday']}\n"
                                          f"temp_max: {conteudo['results']['forecast'][2]['max']}°C\n"
                                          f"temp_min: {conteudo['results']['forecast'][2]['min']}°C\n"
                                          f"cloudiness: {conteudo['results']['forecast'][2]['cloudiness']}\n"
                                          f"rain: {conteudo['results']['forecast'][2]['rain']} mm\n"
                                          f"rain_probability: {conteudo['results']['forecast'][2]['rain_probability']}%\n"
                                          f"windy_speedy: {conteudo['results']['forecast'][2]['wind_speedy']}\n"
                                          f"description: {conteudo['results']['forecast'][2]['description']}\n"
                                          f"condition: {conteudo['results']['forecast'][2]['condition']}")
    texto_resposta_1.grid(column=5, row=2, padx=10, pady=5)
    return texto_resposta_1


def dia_3(event):
    texto_resposta_1 = Label(janela, text=f"dia: {conteudo['results']['forecast'][3]['date']}/2022\n"
                                          f"dia da semana: {conteudo['results']['forecast'][3]['weekday']}\n"
                                          f"temp_max: {conteudo['results']['forecast'][3]['max']}°C\n"
                                          f"temp_min: {conteudo['results']['forecast'][3]['min']}°C\n"
                                          f"cloudiness: {conteudo['results']['forecast'][3]['cloudiness']}\n"
                                          f"rain: {conteudo['results']['forecast'][3]['rain']} mm\n"
                                          f"rain_probability: {conteudo['results']['forecast'][3]['rain_probability']}%\n"
                                          f"windy_speedy: {conteudo['results']['forecast'][3]['wind_speedy']}\n"
                                          f"description: {conteudo['results']['forecast'][3]['description']}\n"
                                          f"condição: {conteudo['results']['forecast'][3]['condition']}")
    texto_resposta_1.grid(column=5, row=2, padx=10, pady=5)
    return texto_resposta_1


def dia_4(event):
    texto_resposta_1 = Label(janela, text=f"dia: {conteudo['results']['forecast'][4]['date']}/2022\n"
                                          f"dia da semana: {conteudo['results']['forecast'][4]['weekday']}\n"
                                          f"temp_max: {conteudo['results']['forecast'][4]['max']}°C\n"
                                          f"temp_min: {conteudo['results']['forecast'][4]['min']}°C\n"
                                          f"cloudiness: {conteudo['results']['forecast'][4]['cloudiness']}\n"
                                          f"rain: {conteudo['results']['forecast'][4]['rain']} mm\n"
                                          f"rain_probability: {conteudo['results']['forecast'][4]['rain_probability']}%\n"
                                          f"windy_speedy: {conteudo['results']['forecast'][4]['wind_speedy']}\n"
                                          f"description: {conteudo['results']['forecast'][4]['description']}\n"
                                          f"condição: {conteudo['results']['forecast'][4]['condition']}")
    texto_resposta_1.grid(column=5, row=2, padx=10, pady=5)
    return texto_resposta_1


def dia_5(event):
    texto_resposta_1 = Label(janela, text=f"dia: {conteudo['results']['forecast'][5]['date']}/2022\n"
                                          f"dia da semana: {conteudo['results']['forecast'][5]['weekday']}\n"
                                          f"temp_max: {conteudo['results']['forecast'][5]['max']}°C\n"
                                          f"temp_min: {conteudo['results']['forecast'][5]['min']}°C\n"
                                          f"cloudiness: {conteudo['results']['forecast'][5]['cloudiness']}\n"
                                          f"rain: {conteudo['results']['forecast'][5]['rain']} mm\n"
                                          f"rain_probability: {conteudo['results']['forecast'][5]['rain_probability']}%\n"
                                          f"windy_speedy: {conteudo['results']['forecast'][5]['wind_speedy']}\n"
                                          f"description: {conteudo['results']['forecast'][5]['description']}\n"
                                          f"condição: {conteudo['results']['forecast'][5]['condition']}")
    texto_resposta_1.grid(column=5, row=2, padx=10, pady=10)
    return texto_resposta_1


def dia_6(event):
    texto_resposta_1 = Label(janela, text=f"dia: {conteudo['results']['forecast'][6]['date']}/2022\n"
                                          f"dia da semana: {conteudo['results']['forecast'][6]['weekday']}\n"
                                          f"temperatura máxima: {conteudo['results']['forecast'][6]['max']}°C\n"
                                          f"temperatura mínima: {conteudo['results']['forecast'][6]['min']}°C\n"
                                          f"cloudiness: {conteudo['results']['forecast'][6]['cloudiness']}\n"
                                          f"quantidade de chuva: {conteudo['results']['forecast'][6]['rain']} mm\n"
                                          f"probabilidade de chuva: {conteudo['results']['forecast'][6]['rain_probability']}%\n"
                                          f"velocidade do vento: {conteudo['results']['forecast'][6]['wind_speedy']}\n"
                                          f"descrição: {conteudo['results']['forecast'][6]['description']}\n"
                                          f"condição: {conteudo['results']['forecast'][6]['condition']}")
    texto_resposta_1.grid(column=5, row=2, padx=10, pady=10)
    return texto_resposta_1


def dia_7(event):
    texto_resposta_1 = Label(janela, text=f"dia: {conteudo['results']['forecast'][7]['date']}/2022\n"
                                          f"dia da semana: {conteudo['results']['forecast'][7]['weekday']}\n"
                                          f"temperatura máxima: {conteudo['results']['forecast'][7]['max']}°C\n"
                                          f"temperatura mínima: {conteudo['results']['forecast'][7]['min']}°C\n"
                                          f"cloudiness: {conteudo['results']['forecast'][7]['cloudiness']}\n"
                                          f"quantidade de chuva: {conteudo['results']['forecast'][7]['rain']} mm\n"
                                          f"probabilibade de chuva: {conteudo['results']['forecast'][7]['rain_probability']}%\n"
                                          f"velocidade do vento: {conteudo['results']['forecast'][7]['wind_speedy']}\n"
                                          f"descridescriçãoption: {conteudo['results']['forecast'][7]['description']}\n"
                                          f"condição: {conteudo['results']['forecast'][7]['condition']}")
    texto_resposta_1.grid(column=5, row=2, padx=10, pady=10)
    return texto_resposta_1


def dia_8(event):
    texto_resposta_1 = Label(janela, text=f"dia: {conteudo['results']['forecast'][8]['date']}/2022\n"
                                          f"dia da semana: {conteudo['results']['forecast'][8]['weekday']}\n"
                                          f"temperatura máxima: {conteudo['results']['forecast'][8]['max']}°C\n"
                                          f"temperatura mínima: {conteudo['results']['forecast'][8]['min']}°C\n"
                                          f"cloudiness: {conteudo['results']['forecast'][8]['cloudiness']}\n"
                                          f"quantidade de chuva: {conteudo['results']['forecast'][8]['rain']} mm\n"
                                          f"probabilibade de chuva: {conteudo['results']['forecast'][8]['rain_probability']}%\n"
                                          f"velocidade do vento: {conteudo['results']['forecast'][8]['wind_speedy']}\n"
                                          f"descrição: {conteudo['results']['forecast'][8]['description']}\n"
                                          f"condição: {conteudo['results']['forecast'][8]['condition']}")
    texto_resposta_1.grid(column=5, row=2, padx=10, pady=10)
    return texto_resposta_1


def dia_9(event):
    texto_resposta_1 = Label(janela, text=f"dia: {conteudo['results']['forecast'][9]['date']}/2022\n"
                                          f"dia da semana: {conteudo['results']['forecast'][9]['weekday']}\n"
                                          f"temperatura máxima: {conteudo['results']['forecast'][9]['min']}°C\n"
                                          f"temperatura mínima: {conteudo['results']['forecast'][9]['max']}°C\n"
                                          f"cloudiness: {conteudo['results']['forecast'][9]['cloudiness']}\n"
                                          f"quantidade de chuva: {conteudo['results']['forecast'][9]['rain']} mm\n"
                                          f"probabilibade de chuva: {conteudo['results']['forecast'][9]['rain_probability']}%\n"
                                          f"velocidade do vento: {conteudo['results']['forecast'][9]['wind_speedy']}\n"
                                          f"descrição: {conteudo['results']['forecast'][9]['description']}\n"
                                          f"condição: {conteudo['results']['forecast'][9]['condition']}")
    texto_resposta_1.grid(column=5, row=2, padx=10, pady=10)
    return texto_resposta_1


def handle_click(event):
    texto_resposta = Label(janela, text=f"temperatura: {conteudo['results']['temp']}°C\n"
                                        f"dia: {conteudo['results']['date']}\n"
                                        f"dia da semana: {conteudo['results']['forecast'][0]['weekday']}\n"
                                        f"temp_max: {conteudo['results']['forecast'][0]['max']}°C\n"
                                        f"temp_min: {conteudo['results']['forecast'][0]['min']}°C\n"
                                        f"hora: {conteudo['results']['time']}\n"
                                        f"a descrição do tempo é: {conteudo['results']['description']}\n"
                                        f"e está de: {conteudo['results']['currently']}\n"
                                        f"cidade: {conteudo['results']['city']} \n"
                                        f"umidade: {conteudo['results']['humidity']}%\n"
                                        f"cloudiness: {conteudo['results']['cloudiness']}%\n"
                                        f"chance de chuva de: {conteudo['results']['forecast'][0]['rain_probability']}%\n"
                                        f"quantidade de chuva: {conteudo['results']['rain']} mm\n"
                                        f"velodidade do vento de: {conteudo['results']['wind_speedy']}\n"
                                        f"direção do vento de: {conteudo['results']['wind_direction']}°\n"
                                        f"nascer do Sol: {conteudo['results']['sunrise']}\n"
                                        f"pôr do Sol {conteudo['results']['sunset']}.")
    texto_resposta.grid(column=0, row=2, padx=10, pady=10)

    button1 = Button(janela, text=f"dia {dia + 1}")
    button1.grid(column=1, row=1, padx=10, pady=10)
    button1.bind("<Button-1>", dia_1)

    button2 = Button(janela, text=f"dia {dia + 2}")
    button2.grid(column=2, row=1, padx=10, pady=10)
    button2.bind("<Button-1>", dia_2)

    button3 = Button(janela, text=f"dia {dia + 3}")
    button3.grid(column=3, row=1, padx=10, pady=10)
    button3.bind("<Button-1>", dia_3)

    button4 = Button(janela, text=f"dia {dia + 4}")
    button4.grid(column=4, row=1, padx=10, pady=10)
    button4.bind("<Button-1>", dia_4)

    button5 = Button(janela, text=f"dia {dia + 5}")
    button5.grid(column=5, row=1, padx=10, pady=10)
    button5.bind("<Button-1>", dia_5)

    button6 = Button(janela, text=f"dia {dia + 6}")
    button6.grid(column=6, row=1, padx=10, pady=10)
    button6.bind("<Button-1>", dia_6)

    button7 = Button(janela, text=f"dia {dia + 7}")
    button7.grid(column=7, row=1, padx=10, pady=10)
    button7.bind("<Button-1>", dia_7)

    button8 = Button(janela, text=f"dia {dia + 8}")
    button8.grid(column=8, row=1, padx=10, pady=10)
    button8.bind("<Button-1>", dia_8)

    button9 = Button(janela, text=f"dia {dia + 9}")
    button9.grid(column=9, row=1, padx=10, pady=10)
    button9.bind("<Button-1>", dia_9)

    return texto_resposta


scroll_bar = Scrollbar(janela)

button = Button(janela, text=f"dia {dia}")
button.grid(column=0, row=1, padx=10, pady=10)
button.bind("<Button-1>", handle_click)

janela.mainloop()
