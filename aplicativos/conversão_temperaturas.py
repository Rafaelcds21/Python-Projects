import tkinter as tk
from tkinter import ttk


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return ((fahrenheit-32)*5/9)+273.15


def kelvin_to_fahrenheit(kelvin):
    return ((kelvin-273.15)*9/5)+32


def celsius_to_generica(celsius, pnt_fusao, pnt_ebulicao):
    '''
    [(c-0)/(100-0)] = [(G-fusão)/(ebulicão-fusão)]
    
    G-fusão = [(c/100)*(ebulicão-fusão)]
    
    G = [(c/100)*(ebulicão-fusão)]+fusão
    
    G = (c*(ebulicão-fusão)/100)+fusão  
    '''

    return (celsius*(pnt_ebulicao-pnt_fusao)/100) + pnt_fusao


def fahrenheit_to_generica(fahrenheit, pnt_fusao, pnt_ebulicao):
    '''
    [(f-32)/(212-32)] = [(G-fusão)/(ebulicão-fusão)]

    G-fusão = [((f-32)/180)*(ebulicão-fusão)]

    G = [((f-32)/180)*(ebulicão-fusão)]+fusão

    G = ((f-32)*(ebulicão-fusão)/180)+fusão
    '''

    return (((fahrenheit-32)*(pnt_ebulicao-pnt_fusao))/180)+pnt_fusao


def kelvin_to_generica(kelvin, pnt_fusao, pnt_ebulicao):
    '''
    [(k-273)/(373-273)] = [(G-fusão)/(ebulicão-fusão)]

    G-fusão = [((k-273)/100)*(ebulicão-fusão)]

    G = [((k-273)/100)*(ebulicão-fusão)]+fusão

    G = ((k-273)*(ebulicão-fusão)/100)+fusão
    '''

    return (((kelvin-273.15)*(pnt_ebulicao-pnt_fusao))/100)+pnt_fusao


def generica_to_celsius(temp_generica, pnt_fusao, pnt_ebulicao):
    '''
    [(c-0)/(100-0)] = [(G-fusão)/(ebulicão-fusão)]

    c/100 = [(G-fusão)/(ebulicão-fusão)]

    c = [(G-fusão)/(ebulicão-fusão)]*100
    '''

    return ((temp_generica-pnt_fusao)/(pnt_ebulicao-pnt_fusao))*100


def generica_to_fahrenheit(temp_generica, pnt_fusao, pnt_ebulicao):
    '''
    [(f-32)/(212-32)] = [(G-fusão)/(ebulicão-fusão)]

    (f-32)/180 = [(G-fusão)/(ebulição-fusão)]

    f-32 = [(G-fusão)/(ebulição-fusão)]*180

    f = {[(G-fusão)/(ebulição-fusão)]*180}+32
    '''

    return (((temp_generica-pnt_fusao)/(pnt_ebulicao-pnt_fusao))*180)+32


def generica_to_kelvin(temp_generica, pnt_fusao, pnt_ebulicao):
    '''
    [(k-273)/(373-273)] = [(G-fusão)/(ebulicão-fusão)]

    [(k-273)/100] = [(G-fusão)/(ebulicão-fusão)]

    k-273 = [(G-fusão)/(ebulicão-fusão)]*100

    k = {[(G-fusão)/(ebulicão-fusão)]*100}+273
    '''

    return (((temp_generica-pnt_fusao)/(pnt_ebulicao-pnt_fusao))*100)+273.15


def generica_to_generica():
    '''
    [(G-fusão)/(ebulicão-fusão)] = [(G-fusão)/(ebulicão-fusão)]
    '''

    return None


def converter():
    def aplique():
        pnt_fusao = pnt_fusao_generica_input.get()
        pnt_ebulicao = pnt_ebulicao_generica_input.get()

        if '.' or ',' in pnt_fusao:
            pnt_fusao = float(pnt_fusao)
        else:
            pnt_fusao = int(pnt_fusao)

        if '.' or ',' in pnt_ebulicao:
            pnt_ebulicao = float(pnt_ebulicao)
        else:
            pnt_ebulicao = int(pnt_ebulicao)

        if escala_inicio_selected_option == 'Celsius':
            resposta = celsius_to_generica(celsius=valor, pnt_fusao=pnt_fusao, pnt_ebulicao=pnt_ebulicao)
            resposta_lbl.config(text=f'{resposta} °(Símbolo da escala Genérica)')

        elif escala_inicio_selected_option == 'Fahrenheit':
            resposta = fahrenheit_to_generica(fahrenheit=valor, pnt_fusao=pnt_fusao, pnt_ebulicao=pnt_ebulicao)
            resposta_lbl.config(text=f'{resposta} °(Símbolo da escala Genérica)')

        elif escala_inicio_selected_option == 'Kelvin':
            resposta = kelvin_to_generica(kelvin=valor, pnt_fusao=pnt_fusao, pnt_ebulicao=pnt_ebulicao)
            resposta_lbl.config(text=f'{resposta} °(Símbolo da escala Genérica)')

    resposta_lbl.config(text='')

    escala_inicio_selected_option = escala_inicio_var.get()
    escala_destino_selected_option = escala_destino_var.get()

    valor = str(valor_escala_inicio.get())

    if '.' in valor:
        valor = float(valor)
    else:
        valor = int(valor)

    if escala_inicio_selected_option == 'Celsius' and escala_destino_selected_option == 'Fahrenheit':
        resposta = celsius_to_fahrenheit(celsius=valor)
        resposta_lbl.config(text=f'{resposta} °F')

    elif escala_inicio_selected_option == 'Celsius' and escala_destino_selected_option == 'Kelvin':
        resposta = celsius_to_kelvin(celsius=valor)
        resposta_lbl.config(text=f'{resposta} K')

    elif escala_inicio_selected_option == 'Celsius' and escala_destino_selected_option == 'Genérica':
        resposta_lbl.grid_forget()

        resposta_lbl.grid(row=6, column=0, columnspan=4)

        pnt_fusao_generica_lbl = tk.Label(janela, text='Insira o ponto de fusão da escala genérica: ')
        pnt_fusao_generica_lbl.grid(row=3, column=0)

        pnt_fusao_generica_input = tk.Entry(janela)
        pnt_fusao_generica_input.grid(row=3, column=1)

        pnt_ebulicao_generica_lbl = tk.Label(janela, text='Insira o ponto de ebulicão da escala genérica: ')
        pnt_ebulicao_generica_lbl.grid(row=4, column=0)

        pnt_ebulicao_generica_input = tk.Entry(janela)
        pnt_ebulicao_generica_input.grid(row=4, column=1)

        aplicar_btn = tk.Button(janela, text='Aplicar pontos de fusão e ebulição e converter.',
                                command=aplique)
        aplicar_btn.grid(row=5, column=0, columnspan=4)

    elif escala_inicio_selected_option == 'Fahrenheit' and escala_destino_selected_option == 'Celsius':
        resposta = fahrenheit_to_celsius(fahrenheit=valor)
        resposta_lbl.config(text=f'{resposta} °C')

    elif escala_inicio_selected_option == 'Fahrenheit' and escala_destino_selected_option == 'Kelvin':
        resposta = fahrenheit_to_kelvin(fahrenheit=valor)
        resposta_lbl.config(text=f'{resposta} K')

    elif escala_inicio_selected_option == 'Fahrenheit' and escala_destino_selected_option == 'Genérica':
        resposta_lbl.grid_forget()

        resposta_lbl.grid(row=6, column=0, columnspan=4)

        pnt_fusao_generica_lbl = tk.Label(janela, text='Insira o ponto de fusão da escala genérica: ')
        pnt_fusao_generica_lbl.grid(row=3, column=0)

        pnt_fusao_generica_input = tk.Entry(janela)
        pnt_fusao_generica_input.grid(row=3, column=1)

        pnt_ebulicao_generica_lbl = tk.Label(janela, text='Insira o ponto de ebulicão da escala genérica: ')
        pnt_ebulicao_generica_lbl.grid(row=4, column=0)

        pnt_ebulicao_generica_input = tk.Entry(janela)
        pnt_ebulicao_generica_input.grid(row=4, column=1)

        aplicar_btn = tk.Button(janela, text='Aplicar pontos de fusão e ebulição e converter.',
                                command=aplique)
        aplicar_btn.grid(row=5, column=0, columnspan=4)

    elif escala_inicio_selected_option == 'Kelvin' and escala_destino_selected_option == 'Celsius':
        resposta = kelvin_to_celsius(kelvin=valor)
        resposta_lbl.config(text=f'{resposta} °C')

    elif escala_inicio_selected_option == 'Kelvin' and escala_destino_selected_option == 'Fahrenheit':
        resposta = kelvin_to_fahrenheit(kelvin=valor)
        resposta_lbl.config(text=f'{resposta} °F')

    elif escala_inicio_selected_option == 'Kelvin' and escala_destino_selected_option == 'Genérica':
        resposta_lbl.grid_forget()

        resposta_lbl.grid(row=6, column=0, columnspan=4)

        pnt_fusao_generica_lbl = tk.Label(janela, text='Insira o ponto de fusão da escala genérica: ')
        pnt_fusao_generica_lbl.grid(row=3, column=0)

        pnt_fusao_generica_input = tk.Entry(janela)
        pnt_fusao_generica_input.grid(row=3, column=1)

        pnt_ebulicao_generica_lbl = tk.Label(janela, text='Insira o ponto de ebulicão da escala genérica: ')
        pnt_ebulicao_generica_lbl.grid(row=4, column=0)

        pnt_ebulicao_generica_input = tk.Entry(janela)
        pnt_ebulicao_generica_input.grid(row=4, column=1)

        aplicar_btn = tk.Button(janela, text='Aplicar pontos de fusão e ebulição e converter.',
                                command=aplique)
        aplicar_btn.grid(row=5, column=0, columnspan=4)


janela = tk.Tk()

janela.title('Conversor de temperaturas')

escala_inicio_lbl = tk.Label(janela, text='Escolha a escala de início: ')
escala_inicio_lbl.grid(row=0, column=0)

escala_inicio_var = tk.StringVar()
escala_inicio = ttk.Combobox(janela, textvariable=escala_inicio_var, values=['Celsius',
                                                                             'Fahrenheit',
                                                                             'Kelvin',
                                                                             'Genérica'])
escala_inicio.grid(row=0, column=1)

valor_escala_inicio_lbl = tk.Label(janela, text='Insira o valor a ser convertido: ')
valor_escala_inicio_lbl.grid(row=0, column=2)

valor_escala_inicio = tk.Entry(janela)
valor_escala_inicio.grid(row=0, column=3)

escala_destino_lbl = tk.Label(janela, text='Escolha a escala de destino: ')
escala_destino_lbl.grid(row=1, column=0)

escala_destino_var = tk.StringVar()
escala_destino = ttk.Combobox(janela, textvariable=escala_destino_var, values=['Celsius',
                                                                               'Fahrenheit',
                                                                               'Kelvin',
                                                                               'Genérica'])
escala_destino.grid(row=1, column=1)

conveter_button = tk.Button(janela, text='Converter', command=converter)
conveter_button.grid(row=2, column=0, columnspan=4)

resposta_lbl = tk.Label(janela, text='')
resposta_lbl.grid(row=3, column=0, columnspan=4)

janela.mainloop()
