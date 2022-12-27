import random
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

TOKEN = 'MTA1NTQ3ODM4OTk3ODQzOTc1MA.GSaZsU.-7VAO-aaO1vyz4TBFOpwb--8O4qoKOL5EGTAHU'

client.run(os.getenv('MTA1NTQ3ODM4OTk3ODQzOTc1MA.GSaZsU.-7VAO-aaO1vyz4TBFOpwb--8O4qoKOL5EGTAHU'))

dado = str(input()).lower()

qtde_dados = int(dado.split('d')[0])
tipo_dado = int(dado.split('d')[1].split('+')[0])
bonus = int(dado.split('d')[1].split('+')[1])

lista_tipo_dado = []
lista_qtde_dado = []

for i in range(1, tipo_dado+1):
    lista_tipo_dado.append(i)

for i in range(1, qtde_dados+1):
    numero_escolhido = random.choice(lista_tipo_dado)
    lista_qtde_dado.append(numero_escolhido)

soma_sem_bonus = sum(lista_qtde_dado)
soma = soma_sem_bonus + bonus

print(soma)
