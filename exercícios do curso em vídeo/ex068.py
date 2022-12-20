from random import choice

cont_user_win = 0

while True:
    quem_comeca = [0, 1]
    escolhido = choice(quem_comeca)

    if escolhido == 0:
        lista_maquina_txt = ['par', 'ímpar']
        escolha_maquina_txt = choice(lista_maquina_txt)

        print(f"Eu escolho {escolha_maquina_txt}.")

        escolha_usuario_txt = str(input("Digite a sua escolha: ")).lower()

        if escolha_usuario_txt == escolha_maquina_txt:
            print("Escolha a outra opção!")
            escolha_usuario_txt = str(input("Digite a sua escolha: ")).lower()
    else:
        escolha_usuario_txt = str(input("Digite a sua escolha (par ou ímpar): ")).lower()

        if escolha_usuario_txt == 'par':
            escolha_maquina_txt = 'ímpar'
            print('Eu escolho ímpar.')
        elif escolha_usuario_txt == 'ímpar' or 'impar':
            escolha_maquina_txt = 'par'
            print('Eu escolho par.')

    lista_maquina_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    numero_escolhido_maquina = choice(lista_maquina_num)

    numero_escolhido_usuario = int(input('Digite um número: '))

    soma = numero_escolhido_usuario + numero_escolhido_maquina

    if soma % 2 == 0 and escolha_maquina_txt == 'par':
        print(f"Eu ganhei! Você escolheu {escolha_usuario_txt} e jogou {numero_escolhido_usuario}, eu escolhi "
              f"{escolha_maquina_txt} e joguei {numero_escolhido_maquina}, a soma foi {soma} que é par")
        break

    elif soma % 2 == 0 and escolha_usuario_txt == 'par':
        print(f"Você ganhou! Você escolheu {escolha_usuario_txt} e jogou {numero_escolhido_usuario}, eu escolhi "
              f"{escolha_maquina_txt} e joguei {numero_escolhido_maquina}, a soma foi {soma} que é par")
        cont_user_win += 1

    elif soma % 2 == 1 and escolha_maquina_txt == 'ímpar' or 'impar':
        print(f"Eu ganhei! Você escolheu {escolha_usuario_txt} e jogou {numero_escolhido_usuario}, eu escolhi "
              f"{escolha_maquina_txt} e joguei {numero_escolhido_maquina}, a soma foi {soma} que é ímpar")
        break

    elif soma % 2 == 1 and escolha_usuario_txt == 'ímpar' or 'impar':
        print(f"Você ganhou! Você escolheu {escolha_usuario_txt} e jogou {numero_escolhido_usuario}, eu escolhi "
              f"{escolha_maquina_txt} e joguei {numero_escolhido_maquina}, a soma foi {soma} que é ímpar")
        cont_user_win += 1

print(f'Você ganhou {cont_user_win} vezes consecutivas.')

