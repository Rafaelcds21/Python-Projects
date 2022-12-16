import pyshorteners

url = input('Insira a url do vídeo: ')

s = pyshorteners.Shortener()

shortUrl = s.tinyurl.short(url)

print(f'URL encurtada: {shortUrl}')
