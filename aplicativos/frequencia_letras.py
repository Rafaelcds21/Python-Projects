import matplotlib.pyplot as plt

texto = str(input("Insira um texto: ")).lower()
print(texto)

palavra_car_esp = texto.split(" ")
print(palavra_car_esp)

lista_palavra = []

for i in range(0, len(palavra_car_esp)):
    palavra = ''

    if ',' in palavra_car_esp[i]:
        palavra = palavra_car_esp[i].split(",")[0]
    elif '!' in palavra_car_esp[i]:
        palavra = palavra_car_esp[i].split("!")[0]
    else:
        palavra = palavra_car_esp[i]

    lista_palavra.append(palavra)

    print(palavra[0])

print(lista_palavra)

lista_letras = []

for i in range(0, len(lista_palavra)):
    letras = list(lista_palavra[i])

    print(letras)

    for j in range(0, len(letras)):
        lista_letras.append(letras[j])

        print(letras)

print(lista_letras)

cont_a = 0
cont_b = 0
cont_c = 0
cont_d = 0
cont_e = 0
cont_f = 0
cont_g = 0
cont_h = 0
cont_i = 0
cont_j = 0
cont_k = 0
cont_l = 0
cont_m = 0
cont_n = 0
cont_o = 0
cont_p = 0
cont_q = 0
cont_r = 0
cont_s = 0
cont_t = 0
cont_u = 0
cont_v = 0
cont_w = 0
cont_x = 0
cont_y = 0
cont_z = 0

lista_frequencia = []

for i in range(0, len(lista_letras)):
    if lista_letras[i] == 'a':
        cont_a += 1
    elif lista_letras[i] == 'b':
        cont_b += 1
    elif lista_letras[i] == 'c':
        cont_c += 1
    elif lista_letras[i] == 'd':
        cont_d += 1
    elif lista_letras[i] == 'e':
        cont_e += 1
    elif lista_letras[i] == 'f':
        cont_f += 1
    elif lista_letras[i] == 'g':
        cont_g += 1
    elif lista_letras[i] == 'h':
        cont_h += 1
    elif lista_letras[i] == 'i':
        cont_i += 1
    elif lista_letras[i] == 'j':
        cont_j += 1
    elif lista_letras[i] == 'k':
        cont_k += 1
    elif lista_letras[i] == 'l':
        cont_l += 1
    elif lista_letras[i] == 'm':
        cont_m += 1
    elif lista_letras[i] == 'n':
        cont_n += 1
    elif lista_letras[i] == 'o':
        cont_o += 1
    elif lista_letras[i] == 'p':
        cont_p += 1
    elif lista_letras[i] == 'q':
        cont_q += 1
    elif lista_letras[i] == 'r':
        cont_r += 1
    elif lista_letras[i] == 's':
        cont_s += 1
    elif lista_letras[i] == 't':
        cont_t += 1
    elif lista_letras[i] == 'u':
        cont_u += 1
    elif lista_letras[i] == 'v':
        cont_v += 1
    elif lista_letras[i] == 'w':
        cont_w += 1
    elif lista_letras[i] == 'x':
        cont_x += 1
    elif lista_letras[i] == 'y':
        cont_y += 1
    elif lista_letras[i] == 'z':
        cont_z += 1

lista_frequencia.append(cont_a)
lista_frequencia.append(cont_b)
lista_frequencia.append(cont_c)
lista_frequencia.append(cont_d)
lista_frequencia.append(cont_e)
lista_frequencia.append(cont_f)
lista_frequencia.append(cont_g)
lista_frequencia.append(cont_h)
lista_frequencia.append(cont_i)
lista_frequencia.append(cont_j)
lista_frequencia.append(cont_k)
lista_frequencia.append(cont_l)
lista_frequencia.append(cont_m)
lista_frequencia.append(cont_n)
lista_frequencia.append(cont_o)
lista_frequencia.append(cont_p)
lista_frequencia.append(cont_q)
lista_frequencia.append(cont_r)
lista_frequencia.append(cont_s)
lista_frequencia.append(cont_t)
lista_frequencia.append(cont_u)
lista_frequencia.append(cont_v)
lista_frequencia.append(cont_w)
lista_frequencia.append(cont_x)
lista_frequencia.append(cont_y)
lista_frequencia.append(cont_z)

print(lista_frequencia)

plt.hist(lista_frequencia)
plt.title("Frequência de letras de um texto")
plt.xlabel("Letras")
plt.ylabel("Frequência")
plt.show()
