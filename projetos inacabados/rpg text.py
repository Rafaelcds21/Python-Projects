import time

# Dividir em 'capítulos', penso que será mais econômico, clean e de fácil manutenção e aprimoramento. Mudar de capítulos
# em checkpoints.

# Capítulo 1: Começa com o player na caverna, passa pela construção de ferramentas rústicas e termina com a construção
# do 1° acampamento.
# Capítulo 2: Parte 
# Capítulo 3:


def rules():
    print('Você terá 5 ações por dia. Quando o aviso de fome aparecer na tela, você terá 3 ações para comer ou morrerá')


def sugestao():
    print('Procure por locais seguros, busque recursos e sobreviva')


def inventario():
    print('Você tem 0 itens.')


def parte1():
    input1 = str(input('Você acordar no meio da mata. O que você faz: '))

    if 'sair' in input1:
        flag = False
    elif '/rules' in input1:
        rules()
    elif 'levantar' in input1:
        print('Você está em uma caverna. Só a 1 caminho para seguir, para frente.')
        input2 = str(input('O que deseja fazer? '))
        if 'frente' in input2:
            print('Você chega na porta da caverna e há mato na sua frente e ao seu redor.')
            input3 = str(input('O que deseja fazer? '))
            if 'procurar' and 'local' in input3:
                print('Você procura por um local seguro e depois de algumas horas encontra uma clareira')
                input4 = str(input('O quê deseja fazer? '))



print('-'*25)
print('Dr. Stone game')
print('-'*25)

print('Bem vindo ao jogo. Sempre que quiser checar as regras digite "/rules" e para pedir sugestões digite /sugestao.')
inicio = str(input('Deseja começar?')).lower()

flag = True

while flag:
    if 'sim' in inicio:
        parte1()

    else:
        flag = False
