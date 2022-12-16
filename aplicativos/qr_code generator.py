import qrcode
from PIL import Image
from pyzbar.pyzbar import decode


def criar_qrcode():
    # Próxima melhoria - Enviar para o diretório principal do pc

    data = input('Insira o que vai ser transformado em qr code: ')
    img = qrcode.make(data)
    img.save('My QR code 1.png')
    print('QRCode gerado.')


def ler_qrcode():
    read = decode(Image.open('My QR code 1.png'))
    print(read[0].data)


flag = True

while flag:
    pergunta = str(input("Para gerar um qrcode digite 'gerar', para extrair o texto de um qrcode digite 'extrair' ")).lower()

    if pergunta == 'gerar':
        criar_qrcode()

    elif pergunta == 'extrair':
        ler_qrcode()

    else:
        reinicio = str(input('Insira uma resposta válida. Digite "sim" para reiniciar ou "não" para sair: ')).lower()
        if reinicio == 'sim':
            continue
        elif reinicio == 'não' or 'nao':
            flag = False
