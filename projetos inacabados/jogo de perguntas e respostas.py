from tkinter import *
import random


def btn_onclick():
    def mostrar_resposta():
        resposta_predefinida = pergunta_random[1][0]

        resposta_usuario = str(inp_resposta.get())

        if resposta_usuario == resposta_predefinida:
            resposta_tela['text'] = 'Muito bem'

        else:
            resposta_tela['text'] = 'Tente novamente'

    inp_assunto = assunto.get()

    lista = 0

    if inp_assunto == 'historia' or inp_assunto == 'história':
        lista = lista_historia

    elif inp_assunto == 'geografia':
        lista = lista_geografia

    elif inp_assunto == 'fisica' or inp_assunto == 'física':
        lista = lista_fisica

    elif inp_assunto == 'matemática' or inp_assunto == 'matematica':
        lista = lista_matematica

    elif inp_assunto == 'inglês' or inp_assunto == 'ingles':
        lista = lista_ingles

    pergunta_random = random.choice(lista)

    pergunta['text'] = pergunta_random[0]

    inp_resposta = Entry(janela)
    inp_resposta.grid(column=1, row=1)

    button2 = Button(janela, height=1, width=10, text='responder', command=mostrar_resposta)
    button2.grid(column=2, row=1)

    resposta_tela = Label(janela, text='')
    resposta_tela.grid(column=3, row=0)

    return inp_assunto


lista_historia = [['Em que ano o ser Humano pisou na Lua?', ['1969']]]
lista_geografia = [['A Terra é redonda?', ['sim']]]
lista_fisica = [['Quais são os tipos de lentes?', ['convergente e divergente', 'divergente e convergente',
                                                   'convergentes e divergentes', 'divergentes e convergentes']]]
lista_matematica = [['Quanto é 1+1?', ['2']], ['Qual é a deriva de 1/x?', ['ln(x)']]]
lista_ingles = [['Como se diz "mesa" em inglês?', ['table']]]

janela = Tk()

janela.title("Quiz")
janela.geometry("500x500")

assunto_txt = Label(janela, text='Insira o assunto:')
assunto_txt.grid(column=0, row=0)

assunto = Entry(janela)
assunto.grid(column=1, row=0)

button = Button(janela, height=1, width=10, text='continuar', command=btn_onclick)
button.grid(column=2, row=0)

pergunta = Label(janela, text='')
pergunta.grid(column=0, row=1)

janela.mainloop()
