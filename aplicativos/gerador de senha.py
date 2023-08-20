from random import sample, choice
import tkinter as tk


def gerar_senha():
    char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9]

    senha_list = sample(char_list, int(entrada.get()))
    senha = ''

    for char in senha_list:
        if type(char) == str:
            tamanho_letra = choice(['upper', 'lower'])
            if tamanho_letra == 'upper':
                char = char.upper()
            elif tamanho_letra == 'lower':
                char = char.lower()
        senha += f'{char}'

    resultado = tk.Label(janela, text=f'Senha = {senha}')
    resultado.grid(row=1, column=0, columnspan=3)


janela = tk.Tk()

lbl = tk.Label(janela, text='Insira a quantidade de dígitos:')
lbl.grid(row=0, column=0)

entrada = tk.Entry(janela)
entrada.grid(row=0, column=1)

button = tk.Button(janela, text='Gerar senha', command=gerar_senha)
button.grid(row=0, column=2)

janela.mainloop()
