import os
from os import system
from pathlib import Path


ruta = Path(Path.home(), 'Recetas')

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob('**/*.txt'):
        contador += 1
    return contador


def inicio():
    eleccion_menu = 'x'
    
    system('cls')
    print('*' * 43)
    print('* Bienvenido al administrador de recetas! *')
    print('*' * 43)
    print('\n')
    print(f'Las recetas se encuentran en {ruta}')
    print(f'Total de recetas: {contar_recetas(ruta)}')
    
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print('Elige una opcion: ')
        print('''
              1) Leer receta
              2) Crear nueva receta
              3) Nueva categoria
              4) Eliminar receta
              5) Elminar categoria
              6) Salir del programa
              ''')
        eleccion_menu = input()
    return eleccion_menu
    

def mostrar_categorias(ruta):
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    
    print('Categorias:')
    
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'{contador} - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
    
    return lista_categorias


def elegir_categorias(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nElige una categoria: ')
    return lista[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta):
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    print('Recetas: ')
    
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'{contador} - {receta_str}')
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas


def elegir_receta(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) - 1):
        eleccion_correcta = input('\nElige una receta: ')
    return lista[int(eleccion_correcta) - 1]
        


# Mostrar menu inicio
menu = 0

match menu:
    case 1:
        mis_categorias = mostrar_categorias(ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        # leer recetas
        # volver inicio
        pass
    case 2:
        mis_categorias = mostrar_categorias(ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        # crear receta nueva
        # volver inicio
        pass
    case 3:
        # crear categoria nueva
        # volver inicio
        pass
    case 4:
        mis_categorias = mostrar_categorias(ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        # eliminar recetas
        # volver inicio
        pass
    case 5:
        mis_categorias = mostrar_categorias(ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        # eliminar categoria
        # volver inicio
        pass
    case 6:
        # finalizar programa
        pass