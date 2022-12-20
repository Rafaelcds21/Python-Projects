tupla_time = ('flamengo', 'vasco', 'botafogo', 'fluminense', 'chapecoense', 'piracicaba', 'a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n')

# a
for i in range(0, 5):
    print(f'{i+1}°: {tupla_time[i]}')

# b
for i in range(16, 20):
    print(f'{i}°: {tupla_time[i]}')

# c

# d
print(f"{tupla_time.index('chapecoense')+1}° posição")
