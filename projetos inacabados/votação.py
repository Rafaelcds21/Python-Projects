print("#################################################")
print("PROJETO URNA ELETRONICA")
print("Nome: Maria e Giulia TIA:42207691/42205697")
print("#################################################")

# LISTAS QUE VAO ARMAZENAS TODA A INFORMAÇÃO DOS CANDIDATOS (NOME PARTIDO CARGO E NUMERO)
presidente = []
governador = []
prefeito = []
eleitor = []

# LISTAS QUE VAO ARMAZENAR OS VOTOS EM CADA CARGO
armazenapresi = []
armazenagov = []
armazenaprefe = []
amarzenaeleitor = []
sair = 0

########################


def canditados():
    continuar = 0
    while continuar != "não":
        nomec = input("Digite o NOME do candidato: ")
        numero = int(input("Digite o numero do canditado: "))
        partido = input("Digite a SIGLA do partido: ")
        cargo = input("Digte o CARGO do canditado (prefeito, governador ou presidente): ")

        if cargo == "presidente":
            presidente.append(nomec)
            presidente.append(numero)
            presidente.append(partido)
            ok = 1
        elif cargo == "governador":
            governador.append(nomec)
            governador.append(numero)
            governador.append(partido)
            ok = 1
        elif cargo == "prefeito":
            prefeito.append(nomec)
            prefeito.append(numero)
            prefeito.append(partido)
            ok = 1
        else:
            print("Insira um cargo válido")

        continuar = input("Deseja adicionar outro candidato (sim ou não)?: ")


def eleitores():
    continuar = 0
    while continuar != "não":
        nomee = input("Digite o nome do eleitor: ")
        cpf = str(input("Digite o CPF do eleitor: "))
        eleitor.append(cpf)

        ok = 1
        continuar = input("Deseja adicionar outro eleitor (sim ou não)?: ")


def votar():
    cont_branco = 0
    cont_nulo = 0
    ok = 0

    print("Caso queira votar EM BRANCO, digite (-1), Caso queira votar NULO, digite (-2)")

    while ok == 0:
        cpf = str(input(" CPF do Eleitor: "))

        votospresi = int(input("\nVOTE PRESIDENTE: "))

        if votospresi == "-1":
            print("VOTO EM BRANCO")

        elif votospresi == "-2":
            print("VOTO NULO")

        else:
            x = presidente.index(votospresi)
            print("CANDIDATO:", presidente[(x - 2)], "/ Partido:", presidente[(x - 1)])

        amarzenaeleitor.append(cpf)
        armazenapresi.append(votospresi)

        confirma = input("Digite (ok) para confirmar seu voto, caso tenha errado, digite (voltar): ")

        if confirma == "ok":
            ok = 1

    while ok == 1:
        votosgov = int(input("\nVOTE GOVERNADOR: "))
        if votosgov == "-1":
            print("VOTO EM BRANCO")

        elif votosgov == "-2":
            print("VOTO NULO")

        else:
            y = governador.index(votosgov)
            print("CANDIDATO:", governador[(y - 2)], "/ Partido:", governador[(y - 1)])

        armazenagov.append(votosgov)

        confirma = input("Digite (ok) para confirmar seu voto, caso tenha errado, digite (voltar): ")

        if confirma == "ok":
            ok = 0

    while ok == 0:
        votosprefe = int(input("\nVOTE PREFEITO: "))

        if votosprefe == "-1":
            print("VOTO EM BRANCO")

        elif votosprefe == "-2":
            print("VOTO NULO")

        else:
            x = prefeito.index(votosprefe)
            print("CANDIDATO:", prefeito[(x - 2)], "/ Partido:", prefeito[(x - 1)])

        armazenaprefe.append(votosprefe)

        confirma = input("Digite (ok) para confirmar seu voto, caso tenha errado, digite (voltar): ")

        if confirma == "ok":
            ok = 1

    return armazenapresi
    return amazenagov
    return armazenaprefe
    return armazenaeleitor


def apurar():
    # print("SOCORRO")
    cand_pres = ''

    # pegar os votos totais para presidentes
    for i in range(0, len(presidente)):
        if i % 3 == 0:
            votos = presidente[i+1]
            cand_pres1 = presidente[i]
            cand_pres = cand_pres1

        elif i % 3 == 1:
            votos = presidente[i]

        elif i % 3 == 2:
            votos = presidente[i-1]

        print(f'O candidato {cand_pres} ganhou')  # {} votos.')

    print(armazenapresi)

    # pegar os votos totais para governadores
    print(armazenagov)

    # pegar os votos totais para prefeitos
    print(armazenaprefe)


def relatorio():
    print("AAA")


while sair == 0:
    print(" MENU - Simulador do sistema de votação ")
    print("\n(1) Cadastrar Candidatos \n(2) Cadastrar Eleitores \n(3) Votar \n(4) Apurar Resultados \n(5) Relatório e "
          "Estatísticas \n(6) Encerrar \n")

    escolha = int(input("Opção escolhida: "))

    if escolha == 1:
        canditados()
        print("\n")

    elif escolha == 2:
        eleitores()
        print("\n")

    elif escolha == 3:
        votar()
        print("\n")

    elif escolha == 4:
        apurar()
        print("\n")

    elif escolha == 5:
        relatorio()
        print("\n")

    elif escolha == 6:
        sair = 1
