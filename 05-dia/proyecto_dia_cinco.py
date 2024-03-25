from random import choice


vidas = 6
intentos = 0
juego_terminado = False
letras_correctas = []
letras_incorrectas = []
palabras = ['paloma', 'manzana', 'tijeras', 'perro', 'computadora']


def elegir_palabra(lista):
    palabra_elegida = choice(lista)
    letras_unicas = len(set(palabra_elegida))
    
    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    
    while not es_valida:
        letra_elegida = input('Ingresa una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('No has elegido una letra correcta.')
        
    return letra_elegida


def mostrar_palabra_oculta(palabra):
    lista_oculta = []
    
    for letra in palabra:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('-')
    
    print(' '.join(lista_oculta))
    

def checar_letra_usuario(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya ingresaste esa letra, intenta con otra.')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
        
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
        
    return vidas, fin, coincidencias


def perder():
    print('Has terminado tus vidas!')
    print(f'La palabra correcta era {palabra}')
    
    return True


def ganar(palabra_correcta):
    mostrar_palabra_oculta(palabra_correcta)
    print('Felicidades! Ganaste la partida')
    
    return True


palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_palabra_oculta(palabra)
    print('\n')
    print(f'Letras incorrectas: {'-'.join(letras_incorrectas)}')
    print(f'Vidas: {vidas}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()
    intents, terminado, aciertos = checar_letra_usuario(letra, palabra, vidas, intentos)
    
    vidas = intents
    intentos = aciertos
    juego_terminado = terminado