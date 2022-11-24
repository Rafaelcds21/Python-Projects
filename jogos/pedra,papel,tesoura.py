import random


def mainloop():
    if player_input == 'pedra':
        if maquina_input == 'pedra':
            print(f'Empate. A sua escolha foi {player_input} e a escolha da máquina foi {maquina_input}')
        elif maquina_input == 'papel':
            print(f'Você perdeu. A sua escolha foi {player_input} e a escolha da máquina foi {maquina_input}')
        else:
            print(f'Você ganhou. A sua escolha foi {player_input} e a escolha da máquina foi {maquina_input}')

    elif player_input == 'papel':
        if maquina_input == 'pedra':
            print(f'Você ganhou. A sua escolha foi {player_input} e a escolha da máquina foi {maquina_input}')
        elif maquina_input == 'papel':
            print(f'Empate. A sua escolha foi {player_input} e a escolha da máquina foi {maquina_input}')
        else:
            print(f'Você perdeu. A sua escolha foi {player_input} e a escolha da máquina foi {maquina_input}')

    else:
        if maquina_input == 'pedra':
            print(f'Você perdeu. A sua escolha foi {player_input} e a escolha da máquina foi {maquina_input}')
        elif maquina_input == 'papel':
            print(f'Você ganhou. A sua escolha foi {player_input} e a escolha da máquina foi {maquina_input}')
        else:
            print(f'Empate. A sua escolha foi {player_input} e a escolha da máquina foi {maquina_input}')


iniciar = input('Deseja iniciar? (sim/não) ').lower()

conjunto = ['pedra', 'papel', 'tesoura']

while True:
    if iniciar == 'sim':
        player_input = str(input('Insira a sua escolha: '))
        maquina_input = random.choice(conjunto)
        mainloop()

    else:
        break

    continuar = input('Você deseja continuar? (sim/não) ')
    iniciar = continuar
