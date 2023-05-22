from random import choice


palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 0
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabrtas):
    palabra_elegida = choice(lista_palabrtas)
    letras_unicas = len(set(palabra_elegida))
    
    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    
    while not es_valida:
        letra_elegida = input('Elije una letra')
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('No has elegido la letra correcta')
            
    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    
    print(' '.join(lista_oculta))
    

def checar_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
        
        if vidas == 0:
            fin = perder()
        elif coincidencias == letras_unicas:
            fin = ganar(palabra_oculta)
            
        return vidas, fin, coincidencias
    

def perder():
    print('Te has quedado sin vidas manix')
    print(f'Wacha ira, la palabra oculta es {palabra}')


def ganar(palabra_descubierta):
    pass


palabra, letras_unicas = elegir_palabra(palabras)

# TODO: Terminar el juego