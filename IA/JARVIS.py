import speech_recognition as sr
import os

# Reconhecer o que se fala
microfone = sr.Recognizer()

# usando o microfone
with sr.Microphone() as source:
    # Chama um algoritmo de reducao de ruidos no som
    microfone.adjust_for_ambient_noise(source)

    # Frase para o usuario dizer algo
    print("Diga alguma coisa: ")

    # Armazena o que foi dito numa variavel
    audio = microfone.listen(source)

# Traduzir para texto
try:
    # Passa a variável para o algoritmo reconhecedor de padroes
    frase = microfone.recognize_google(audio, language='pt-BR')
    if "navegador" in frase:
        os.system("start Chrome.exe")
    elif "Excel" in frase:
        os.system("start Excel.exe")

    # Retorna a frase pronunciada
    print("Você disse: " + frase)
except sr.UnknownValueError:
    print("Não Entendi")
