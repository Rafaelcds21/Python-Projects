seq_fib = "0 - 1 - "+f"{1} - "
print(seq_fib)

soma = 0
qtde_elementos = int(input("Insira um número inteiro: "))
for i in range(1, qtde_elementos+1):
    soma += i
    seq_fib = "0 - 1 - " + f"{soma} - "
    print(seq_fib)

