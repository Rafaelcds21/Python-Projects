import pyttsx3

# iniciando pyttsx3
motor = pyttsx3.init()

rate = motor.getProperty('rate')   # obtendo detalhes da taxa de fala atual
print(rate)                        # imprimindo a taxa de voz atual
motor.setProperty('rate', 125)     # configurando nova taxa de voz

volume = motor.getProperty('volume')  # conhecendo o nível de volume atual (min=0 e max=1)
print(volume)                         # imprimindo o nível de volume atual
motor.setProperty('volume', 1.0)      # configurando o nível de volume entre 0 e 1


# passando pra ele o texto que gostamos de ouvir
frase = input("Insira um texto: ")
vozes = motor.getProperty('voices')       # obtendo detalhes da voz atual
# motor.setProperty('voice', vozes[0].id) # alterando o índice, muda as vozes. 0 para homem
# motor.setProperty('voice', vozes[1].id) # alterando o índice, muda as vozes. 1 para mulher
motor.say(f"{frase}")

# text o texto
motor.runAndWait()
