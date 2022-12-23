from tkinter import *
import functools


class TelaCpfdc(Frame):
    def __init__(self, parent, nome):
        Frame.__init__(self, parent)
        self.nome = nome

        senha_txt = Label(self, text='Insira a quantidade de dígitos que a senha deve ter: ')
        senha_txt.pack()

        senha_inp = Entry(self)
        senha_inp.pack()

        cpf_btn = Button(self, text='Mostrar senha aleatória')  # , command=gerar_senha)
        cpf_btn.pack()

        label_resposta = Label(self, text='')
        label_resposta.pack()


class Menu(Frame):
    def __init__(self, parent, *subtelas):
        Frame.__init__(self, parent)
        self.current_frame = self

        self.figura = Label(self, text='Escolha uma ação:')
        self.figura.pack()

        for subtela in subtelas:
            Button(subtela, text='Voltar', command=functools.partial(self.muda_tela, self)).pack(side=BOTTOM, expand=YES,
                                                                                                 fill=BOTH)
            Button(self, text=subtela.nome, command=functools.partial(self.muda_tela, subtela)).pack()

    def muda_tela(self, qual):
        self.current_frame.pack_forget()
        qual.pack()
        self.current_frame = qual


if __name__ == '__main__':
    root = Tk()
    root.title('')
    root.resizable(height=None, width=None)

    t1 = TelaCpfdc(root, 'Gerador de senha')

    m = Menu(root, t1)
    m.pack()

    root.mainloop()
