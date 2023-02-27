from tkinter import *
import requests
from PIL import ImageTk, Image

api_key = 'aqui vai a sua chave da API'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

response = requests.get(url)
data = response.json()

img_url = data['url']

image_response = requests.get(img_url, stream=True)
image_response.raw.decode_content = True
image = Image.open(image_response.raw)

image = image.resize((400, 400), Image.ANTIALIAS)

root = Tk()
root.title("Imagem do dia da NASA")

text = Label(root, text='Aqui está a foto do dia escolhida pela Nasa!')
text.pack()

canvas = Canvas(root, width=400, height=400)
canvas.pack()

img = ImageTk.PhotoImage(image)
canvas.create_image(200, 200, image=img)

root.mainloop()
