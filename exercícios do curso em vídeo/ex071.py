valor = int(input("Insira o valor: "))

if valor < 10:
    print(f"Serão entregues {valor} moedas de R$1,00")

elif 10 <= valor < 20:
    qtde_nota10 = valor // 10
    qtde_nota1 = valor - 10 * qtde_nota10
    print(f"Serão entregues {qtde_nota10} notas de R$10,00 e {qtde_nota1} moedas de R$1,00")

elif 20 <= valor < 50:
    qtde_nota20 = valor // 20
    qtde_nota10 = (valor - 20 * qtde_nota20) // 10
    qtde_nota1 = valor - 20 * qtde_nota20 - 10 * qtde_nota10
    print(f"Serão entregues {qtde_nota20} notas de R$20,00, {qtde_nota10} notas de R$10,00 e {qtde_nota1} moedas de R$1,00")

elif 50 < valor:
    qtde_nota50 = valor // 50
    qtde_nota20 = (valor - 50 * qtde_nota50) // 20
    qtde_nota10 = (valor - 50 * qtde_nota50 - 20 * qtde_nota20) // 10
    qtde_nota1 = valor - 50 * qtde_nota50 - 20 * qtde_nota20 - 10 * qtde_nota10
    print(f"Serão entregues {qtde_nota50} notas de R$50,00, {qtde_nota20} notas de R$20,00, {qtde_nota10} notas de R$10,00 e {qtde_nota1} moedas de R$1,00")
