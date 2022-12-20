def fatorial(x):
    resp_fatorial = 1
    for i in range(1, x+1):
        resp_fatorial *= i
    return resp_fatorial


num = int(input("Insira um número: "))
fatorial_num = fatorial(num)
print(fatorial_num)
