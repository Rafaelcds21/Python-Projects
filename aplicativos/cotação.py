from tkinter import *
import functools
import xml.etree.ElementTree as ET
import requests


class TelaListaMoeda(Frame):
    def __init__(self, parent, nome):
        Frame.__init__(self, parent)
        self.nome = nome

        cs = Scrollbar(self)
        cs.pack(side=RIGHT, fill=Y)

        tree = ET.parse('nomes_moedas.xml')
        root = tree.getroot()

        lista_moeda_txt = Label(self, text='Lista de moedas disponíveis: ')
        lista_moeda_txt.pack()

        texto = ''

        for i in range(0, 156):
            texto += f"{root[i].attrib.get('name')} - {root[i].text}\n"

        label_lista_moeda = Text(self, font="Arial 10")
        label_lista_moeda.pack()
        label_lista_moeda.insert(0.0, texto)

        label_lista_moeda.config(yscrollcommand=cs.set)
        cs.config(command=label_lista_moeda.yview)


class TelaConversao(Frame):
    def __init__(self, parent, nome):
        def converter():
            sigla_da_moeda_entrada = ''
            sigla_da_moeda_saida = ''

            inp_moeda_entrada = moeda_entrada_value.get()
            inp_moeda_saida = moeda_saida_value.get()

            for i in range(0, 156):
                if inp_moeda_entrada == root[i].text:
                    sigla_da_moeda_entrada1 = root[i].attrib.get('name')
                    sigla_da_moeda_entrada = sigla_da_moeda_entrada1

                if inp_moeda_saida == root[i].text:
                    sigla_da_moeda_saida1 = root[i].attrib.get('name')
                    sigla_da_moeda_saida = sigla_da_moeda_saida1

            texto_conversao = ''

            try:
                requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/last/{sigla_da_moeda_entrada}-{sigla_da_moeda_saida}')
                conteudo = requisicao.json()

                texto_conversao += f"Sigla da moeda de entrada: {conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['code']}\n"
                texto_conversao += f"Sigla da moeda de entrada: {conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['codein']}\n"
                texto_conversao += f"Nome da moeda de entrada/Nome da moeda de saída: {conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['name']}\n"
                texto_conversao += f"Valor máximo: 1 {sigla_da_moeda_entrada} equivale a {conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['high']} {sigla_da_moeda_saida}\n"
                texto_conversao += f"Valor mínimo: 1 {sigla_da_moeda_entrada} equivale a {conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['low']} {sigla_da_moeda_saida}\n"
                texto_conversao += f"Variação:{conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['varBid']}\n"
                texto_conversao += f"Porcentagem de variação: {conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['pctChange']}%\n"
                texto_conversao += f"Valor de compra: {conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['bid']} {sigla_da_moeda_saida}\n"
                texto_conversao += f"Valor de venda: {conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['ask']} {sigla_da_moeda_saida}\n"
                texto_conversao += f"{conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['timestamp']}\n"
                texto_conversao += f"Última atualização: {conteudo[f'{sigla_da_moeda_entrada}{sigla_da_moeda_saida}']['create_date']}\n"
            except:
                texto_conversao += 'Não foi possível converter entre essas duas moedas.'

            cs = Scrollbar(self)
            cs.pack(side=RIGHT, fill=Y)

            label_conversao_moeda = Text(self, font="Arial 10")
            label_conversao_moeda.pack()
            label_conversao_moeda.insert(0.0, texto_conversao)

            label_conversao_moeda.config(yscrollcommand=cs.set)
            cs.config(command=label_conversao_moeda.yview)

        tree = ET.parse('nomes_moedas.xml')
        root = tree.getroot()

        Frame.__init__(self, parent)
        self.nome = nome

        moeda_entrada_txt = Label(self, text='Insira a moeda de entrada: ')
        moeda_entrada_txt.pack()

        moeda_entrada_value = Entry(self)
        moeda_entrada_value.pack()

        moeda_saida_txt = Label(self, text='Insira a moeda de saída: ')
        moeda_saida_txt.pack()

        moeda_saida_value = Entry(self)
        moeda_saida_value.pack()

        button_conversao = Button(self, text='Converter', command=converter)
        button_conversao.pack()


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
    root.title('Conversor de moedas.')
    root.resizable(height=None, width=None)

    t1 = TelaListaMoeda(root, 'Lista de moedas')
    t2 = TelaConversao(root, 'Conversão')

    m = Menu(root, t1, t2)
    m.pack()

    root.mainloop()
