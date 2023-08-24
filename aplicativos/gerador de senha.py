# Importação de todas as bibliotecas que serão necessárias no código
from random import sample, choice
import tkinter as tk
from tkinter import ttk, Tk, Entry, Label, Button, StringVar

# Lista com todos os caracteres básicos para a geração de uma senha
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

char_especiais_list = []


# Função que vai inserir os caracteres especiais
def inserir_caracter_especial():
    char_especial = especiais_entrada.get()
    especiais_entrada.delete(0, tk.END)
    especiais_entrada.insert(0, char_especial)
    especiais_entrada.focus()

    erro_label.config(text='')
    resultado_label.config(text='')

    if len(list(char_especial)) > 1:
        especiais_label.config(text='Insira apenas um caracter especial')
    else:
        try:
            if char_especial in char_list or int(float(char_especial)):
                especiais_label.config(text="Insira apenas caracteres especiais válidos!")

            else:
                char_especiais_list.append(char_especial)
                especiais_label.config(text="Caracter especial inserido com sucesso!")

        except ValueError:
            char_especiais_list.append(char_especial)
            especiais_label.config(text="Caracter especial inserido com sucesso!")


# Função que vai gerar a senha
def gerar_senha():
    global char_list  # Usar a variável global 'char_list'

    # Recebe a entrada da quantidade de dígitos que a senha deve ter
    quantidade_digitos = entrada.get()

    especiais_label.config(text="")

    # Se não receber nada, pede para o usuário digitar um valor válido
    if not quantidade_digitos:
        erro_label.config(text="Por favor, insira um valor válido.")
        return

    # Caso receba alguma coisa, verifica se é um inteiro ao tentar converter para o tipo int, caso contrário pede para o
    # usuário digitar um valor válido
    try:
        quantidade_digitos = int(quantidade_digitos)

    except ValueError:
        erro_label.config(text="Por favor, insira um valor numérico válido.")
        return

    # Recebe quais deverão ser os tipos de letras (maiúsculas, minúsculas ou mistura aleatória), caso não receba nada
    # oede para o usuário selecionar o tipo de letra
    selected_option = tipo_letras_cb_var.get()
    if not selected_option:
        erro_label.config(text="Por favor, selecione um tipo de letra.")
        return

    # Gera a lista com os caracteres que formarão a senha e cria a variável 'senha' como um texto vazio inicialmente
    if len(char_especiais_list) == 0 and quantidade_digitos > 36:
        senha_list = []
        for i in range(quantidade_digitos//36):
            senha_list_i = sample(char_list, i)
            senha_list.append(senha_list_i)

    elif len(char_especiais_list) > 0 and quantidade_digitos > 36:
        senha_list = sample(char_list + char_especiais_list, quantidade_digitos)
    else:
        senha_list = sample(char_list, quantidade_digitos)

    senha = ''

    # Dependendo do tipo de letra selecionada, a senha será diferente. adicionei uma variável que verifica o tipo do
    # caracter, se for string, ele é modificado para somente maiúscula, minúscula, ou uma mistura randômica de ambas
    if selected_option == 'somente maiúsculas':
        for char in senha_list:
            if type(char) == str:
                char = char.upper()

            senha += f'{char}'

    elif selected_option == 'somente minúsculas':
        for char in senha_list:
            senha += f'{char}'

    elif selected_option == 'mistura aleatória':
        for char in senha_list:
            if type(char) == str:
                tamanho_letra = choice(['upper', 'lower'])
                if tamanho_letra == 'upper':
                    char = char.upper()
                elif tamanho_letra == 'lower':
                    char = char.lower()
            senha += f'{char}'

    # Apaga o texto de erro, caso tenha algum
    erro_label.config(text='')
    especiais_label.config(text='')

    # Mostra a senha no seu devido espaço
    resultado_label.config(text=f'Senha = {senha}')


# Inicializa a janela
janela = Tk()
janela.title('Gerador de senhas') # título do App

# Elementos do App
lbl = Label(janela, text='Insira a quantidade de dígitos:')
lbl.grid(row=0, column=0)

entrada = Entry(janela)
entrada.grid(row=0, column=1)

button = Button(janela, text='Gerar senha', command=gerar_senha)
button.grid(row=0, column=2)

tipo_letras_lbl = Label(janela, text='Selecione os tipos de letras que terão na senha:')
tipo_letras_lbl.grid(row=1, column=0)

tipo_letras_cb_var = StringVar()
tipo_letras_cb = ttk.Combobox(janela, textvariable=tipo_letras_cb_var, values=['',
                                                                               'somente maiúsculas',
                                                                               'somente minúsculas',
                                                                               'mistura aleatória'])
tipo_letras_cb.grid(row=1, column=1)

especiais_lbl = Label(janela, text='Insira caracteres especiais (ex: !@#$%&):')
especiais_lbl.grid(row=2, column=0)

especiais_entrada = Entry(janela)
especiais_entrada.grid(row=2, column=1)

especiais_button = Button(janela, text='Inserir caracter especial', command=inserir_caracter_especial)
especiais_button.grid(row=2, column=2)

# Labels de erro, resultado da inserção de possíveis caracteres especiais e a senha gerada
erro_label = Label(janela, text='')
erro_label.grid(row=3, column=0, columnspan=3)

especiais_label = Label(janela, text='')
especiais_label.grid(row=4, column=0, columnspan=3)

resultado_label = Label(janela, text='')
resultado_label.grid(row=5, column=0, columnspan=3)

janela.mainloop()
