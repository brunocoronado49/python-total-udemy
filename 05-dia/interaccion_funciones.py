from random import shuffle

# lista inicial
palitos = ['-', '--', '---', '----']

# mezclar palitos
def mezclar_palitos(lista_palos):
    shuffle(lista_palos)
    return lista_palos

# pedir intento
def tomar_intento():
    intento = ''
    
    while intento not in ['1', '2', '3', '4']:
        intento = input('Ingresa un numero del 1 al 4: ')
        
    return int(intento)

# comprobar intento
def ver_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos.')
    else:
        print('Te salvaste.')
        
    print(f'Te toco el palito: {lista[intento - 1]}')
    
palos_mezclados = mezclar_palitos(palitos)
suerte = tomar_intento()
ver_intento(palos_mezclados, suerte)