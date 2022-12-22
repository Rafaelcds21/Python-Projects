from Bio.Seq import Seq
from Bio.SeqUtils import GC

trecho = Seq("ACGTAGCTACGATCACAGCTA")

#Imprime a sequência
print(f'O trecho digitado foi {trecho}')

# Imprime o tipo de variável da sequência
print(f'O tipo de variável do trecho é {type(trecho)}')

# Imprime o inverso do trecho
print(f'O inverso do trecho {trecho} é {trecho[::-1]}')

# Imprime o complementar do trecho
print(f'O complementar do trecho {trecho} é {trecho.complement()}')

# Imprime o reverso complementar do trecho
print(f'O reverso complementar do trecho {trecho} é {trecho.reverse_complement()}')

# Imprime a trancrição do trecho
print(f'A transcrição do trecho {trecho} é {trecho.transcribe()}')

# Imprime a sequência de proteína
print(f'A sequência de proteína do trecho {trecho} é {trecho.translate()}')

# Imprime a contagem de vezes em que uma determinada parte aparece na sequência
print(f'A quantidade de vezes em que o trecho TACGA apareceu no trecho {trecho} foi {trecho.count("TACGA")} vezes')

# Conversão Seq --> string
print(f'Para converter uma variável do tipo Seq para string, basta usar str(variável), tipo do trecho usando esse '
      f'método: {type(str(trecho))}')

# Conversão string --> Seq
print(f'Para converter uma variável do tipo string para Seq, basta usar Seq(variável), tipo do trecho usando esse '
      f'método: {type(Seq(str(trecho)))}')

#
print(f'{}')
#
print(f'{}')

# Imprime a porcentagem de bases nitrogenadas que são guanina ou citosina
print(f'A porcentagem de bases nitrogenadas que são guanina ou citosina é {"%.2f" % GC(trecho)}%')
