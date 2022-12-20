preco = float(input('Insira o valor do preço do produto: '))
forma_pagamento = str(input('Insira a forma de pagamento: ')).lower()
if 'à vista' or 'a vista' and 'dinheiro' or 'cheque' in forma_pagamento:
    preco = preco-0.1*preco
    print(preco)
elif 'à vista' or 'a vista' and 'cartão' or 'cartao' in forma_pagamento:
    preco = preco - 0.05 * preco
    print(preco)
elif '2x' and 'cartão' or 'cartao' in forma_pagamento:
    print(preco)
elif '3x' and 'cartão' or 'cartao ' in forma_pagamento:
    preco = preco-0.2*preco
    print(preco)
