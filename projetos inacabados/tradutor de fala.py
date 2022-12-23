import speech_recognition as sr
from translate import Translator
from gtts import gTTS

microfone = sr.Recognizer()

with sr.Microphone() as source:
    print('Diga alguma coisa: ')
    audio = microfone.listen(source)

frase = microfone.recognize_google(audio, language='pt')

s = Translator(from_lang="pt-br", to_lang="en")
res = s.translate(f"{frase}")
sound = gTTS(frase)
