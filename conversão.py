print('-'*9)
print('conversão')
print('-'*9)

# converter distância

# saber a unidade atual

unidade_distancia_atual = str(input('Digite a unidade atual: ')).lower()

# tabela de conversões


def metro():
    medida_metro = float(input('Digite a medida: '))

    polegada = 39.3701 * medida_metro
    jarda = 1.093613888889 * medida_metro
    pes = 3.28084 * medida_metro
    milha = 0.00062137152777784086452 * medida_metro
    milha_nautica = 0.00053995709503245226547 * medida_metro

    print(polegada)
    print(jarda)
    print(pes)
    print(milha)
    print(milha_nautica)


def polegada():
    medida_polegada = float(input('Digite a medida: '))

    metro = 0.025400013716002579206 * medida_polegada
    jarda = 0.027777792777780599409 * medida_polegada
    pes = 0.08333337833334178435 * medida_polegada
    milha = 1.578283680555715826e-5 * medida_polegada
    milha_nautica = 1.371491021382428616e-5 * medida_polegada

    print(metro)
    print(jarda)
    print(pes)
    print(milha)
    print(milha_nautica)


def jarda():
    medida_jarda = float(input('Digite a medida: '))

    metro = 0.91440049377609278203 * medida_jarda
    polegada = 36.000019440003654836 * medida_jarda
    pes = 3.0000016200003041256 * medida_jarda
    milha = 0.00056818212500005758903 * medida_jarda
    milha_nautica = 0.00049373676769767424737 * medida_jarda

    print(metro)
    print(polegada)
    print(pes)
    print(milha)
    print(milha_nautica)


def pes():
    medida_pe = float(input('Digite a medida: '))

    metro = 0.30480016459203090884 * medida_pe
    polegada = 12.000006480001216502 * medida_pe
    jarda = 0.3333335133333671374 * medida_pe
    milha = 0.00018939404166668587204 * medida_pe
    milha_nautica = 0.00016457892256589140676 * medida_pe

    print(metro)
    print(polegada)
    print(jarda)
    print(milha)
    print(milha_nautica)


def milha():
    medida_milha = float(input('Digite a medida: '))

    metro = 1609.3448690459231329 * medida_milha
    polegada = 63360.034214406427054 * medida_milha
    jarda = 1760.0009504001784535 * medida_milha
    pes = 5280.0028512005346784 * medida_milha
    milha_nautica = 0.86897671114790664415 * medida_milha

    print(metro)
    print(polegada)
    print(jarda)
    print(pes)
    print(milha_nautica)


def milha_nautica():
    medida_milha_nautica = float(input('Digite a medida: '))

    metro = 1852.0010000801871684 * medida_milha_nautica
    polegada = 72913.425200007375679 * medida_milha_nautica
    jarda = 2025.3729222224269506 * medida_milha_nautica
    pes = 6076.1187666672803971 * medida_milha_nautica
    milhas = 1.1507800694445609047 * medida_milha_nautica

    print(metro)
    print(polegada)
    print(jarda)
    print(pes)
    print(milhas)


# printar o resultado

if unidade_distancia_atual == 'metro' or 'metros':
    metro()

elif unidade_distancia_atual == 'polegada' or 'polegadas':
    polegada()

elif unidade_distancia_atual == 'jarda' or 'jardas':
    jarda()

elif unidade_distancia_atual == 'pé' or 'pe' or 'pés' or 'pes':
    pes()

elif unidade_distancia_atual == 'milha' or 'milhas':
    milha()

elif unidade_distancia_atual == 'milha náutica' or 'milhas náuticas' or 'milha nautica' or 'milhas nauticas':
    milha_nautica()

# converter temperatura

# definir a unidade de temperatura atual
unidade_temperatura_atual = str(input('Digite a unidade de temperatura atual: ')).lower()

# tabela de conversões


def celsius():
    medida_celsius = float(input('Digite a temperatura: '))

    farenheit = (9*medida_celsius/5)+32
    kelvin = medida_celsius + 273

    print(farenheit)
    print(kelvin)


def farenheit():
    medida_farenheit = float(input('Digite a temperatura: '))

    celsius = 5*(medida_farenheit-32)/9
    kelvin = (5*(medida_farenheit-32)/9) + 273

    print(celsius)
    print(kelvin)


def kelvin():
    medida_kelvin = float(input('Digite a temperatura: '))

    celsius = medida_kelvin - 273
    farenheit = (9*(medida_kelvin - 273)/5)+32

    print(celsius)
    print(farenheit)


# printar o resultado
if unidade_temperatura_atual == 'celsius':
    celsius()
if unidade_temperatura_atual == 'farenheit':
    farenheit()
if unidade_temperatura_atual == 'kelvin':
    kelvin()

# converter tempo
unidade_tempo_atual = str(input('Insira a unidade de tempo para ser convertida: '))

# def attosegundo():
# def picosegundo():
# def nanosegundo():
# def microsegundo():
# def milisegundo():


def segundo():
    valor_segundo = int(input('Insira o valor: '))
    minuto = valor_segundo/60
    hora = valor_segundo/3600
    dia = valor_segundo/(3600*24)
    semana = valor_segundo/(3600*24*7)
    mes = valor_segundo/(3600*24*7*30)
    ano = valor_segundo/(3600*24*7*30*12)


def minuto():
    valor_minuto = int(input('Insira o valor:'))


# def hora():
# def dia():
# def semana():
# def mes():
# def ano():
# def decada():
# def seculo():
# def milenio():

# converter velocidade
