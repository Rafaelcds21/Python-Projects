import qrcode

# Próxima melhoria - Enviar para o diretório principal do pc

data = input('Insira o que vai ser transformado em qr code: ')
img = qrcode.make(data)
img.save('My QR code 1.png')

