from hashlib import sha256
import time

def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()

def minerar(num_bloco, transacoes, hash_anterior, qtde_zeros):
    nonce = 0x7eb3199fc147e0f5
    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        meu_hash = aplicar_sha256(texto)
        if meu_hash.startswith("0" * qtde_zeros):
            return nonce, meu_hash
        nonce += 1

if __name__ == "__main__":
    num_bloco = 1
    transacoes = "200"
    qtde_zeros = 1
    hash_anterior = "0x152b6aa680e6c3e1aba2d67014d83451b233012cc921a12080adaede247246f7"
    inicio = time.time()
    resultado = minerar(num_bloco, transacoes, hash_anterior, qtde_zeros)
    print(resultado)
    print(time.time()-inicio)
