from tkinter import *


def massa_ideal(altura_real):
    massaidealmin = 18.5 * (altura_real ** 2)
    massaidealmax = 24.9 * (altura_real ** 2)
    return massaidealmin, massaidealmax


def altura_ideal(massa_real):
    alturaidealmin = (massa_real / 18.5) ** (1 / 2)
    alturaidealmax = (massa_real / 24.9) ** (1 / 2)
    return alturaidealmin, alturaidealmax


def calc_imc():
    if ',' in massa.get():
        massa_value = float(massa.get().replace(',', '.'))
    else:
        massa_value = float(massa.get())

    if ',' in altura.get():
        altura_value = float(altura.get().replace(',', '.'))
    else:
        altura_value = float(altura.get())

    imc = massa_value/(altura_value**2)

    mostrar_resultado = Label(text=f'Seu IMC é {round(imc, 2)}')
    mostrar_resultado.grid(row=2, column=0, columnspan=3)

    massa_ideal_minima, massa_ideal_maxima = massa_ideal(altura_value)
    altura_ideal_minima, altura_ideal_maxima = altura_ideal(massa_value)

    if imc < 18.5:
        text = f"Você possui Magreza. Para a sua altura você deveria ter entre {round(massa_ideal_minima, 2)} Kg e " \
               f"{round(massa_ideal_maxima, 2)} Kg e para o seu peso você deveria ter {round(altura_ideal_minima, 2)}" \
               f" m e {round(altura_ideal_maxima, 2)} m"

    elif 18.5 < imc < 24.9:
        text = f'Você está com um peso ideal para sua altura.'

    elif 25 < imc < 29.9:
        text = f"Você possui Sobrepeso. Para a sua altura você deveria ter entre {round(massa_ideal_minima, 2)} Kg e " \
               f"{round(massa_ideal_maxima, 2)} Kg e para o seu peso você deveria ter {round(altura_ideal_minima, 2)}" \
               f" m e {round(altura_ideal_maxima, 2)} m"

    elif 30 < imc < 34.9:
        text = f"Você possui Obesidade grau I. Para a sua altura você deveria ter entre {round(massa_ideal_minima, 2)}" \
               f" Kg e {round(massa_ideal_maxima, 2)} Kg e para o seu peso você deveria ter " \
               f"{round(altura_ideal_minima, 2)} m e {round(altura_ideal_maxima, 2)} m"

    elif 35 < imc < 39.9:
        text = f"Você possui Obesidade grau II. Para a sua altura você deveria ter entre {round(massa_ideal_minima, 2)}" \
               f" Kg e {round(massa_ideal_maxima, 2)}  Kg e para o seu peso você deveria ter " \
               f"{round(altura_ideal_minima, 2)} m e {round(altura_ideal_maxima, 2)} m"

    elif imc > 40:
        text = f"Você possui Obesidade grau III. Para a sua altura você deveria ter entre {round(massa_ideal_minima, 2)}" \
               f" Kg e {round(massa_ideal_maxima, 2)} Kg e para o seu peso você deveria ter " \
               f"{round(altura_ideal_minima, 2)} m e {round(altura_ideal_maxima, 2)} m"

    res_ideal = Label(text=f'{text}')
    res_ideal.grid(row=3, column=0, columnspan=3)


janela = Tk()

janela.geometry('900x200')
janela.title('Calculadora de IMC')

mass_txt = Label(text='Insira a sua massa (em Kg):')
mass_txt.grid(row=0, column=0)

massa = Entry()
massa.grid(row=0, column=1)

height_txt = Label(text='Insira a sua altura (em m):')
height_txt.grid(row=1, column=0)

altura = Entry()
altura.grid(row=1, column=1)

btn_calc_imc = Button(text='Clique aqui para calcular seu IMC', command=calc_imc)
btn_calc_imc.grid(row=0, column=2, rowspan=2)

janela.mainloop()
