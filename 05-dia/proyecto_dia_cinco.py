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
    letra = ''
    while letra > 1:
        letra = input('Ingresa una letra')
        
    return letra


def palabra_oculta(palabra_lista):
    palabra_guiones = ''
    
    for palabra in palabra_lista:
        palabra_lista += '-'
        
    return palabra_guiones


