flag = True
while flag:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    for i in range(0, 11):
        print(f"{num}x{i}={num*i}")
