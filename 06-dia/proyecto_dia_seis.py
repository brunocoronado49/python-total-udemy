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
    return int(eleccion_menu)
    

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


def leer_receta(receta):
    print(Path.read_text(receta))
    

def crear_receta(ruta):
    existe = False
    
    while not existe:
        print('Escribe el nombre de tu receta: ')
        nombre_receta = input() + '.txt'
        print('Escribe la receta: ')
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} se ha creado')
            existe = True
        else:
            print('Esa receta ya existe')
            
            
def crear_categoria(ruta):
    existe = False
    
    while not existe:
        print('Escribe el nombre de tu receta: ')
        nombre_categoria = input() + '.txt'
        ruta_nueva = Path(ruta, nombre_categoria)
        
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu categoria {nombre_categoria} se ha creado')
            existe = True
        else:
            print('Esa categoria ya existe')
            
            
def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name} se ha eliminado')
    

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoria {categoria.name} se ha eliminado')
    
    
def volver_inicio():
    eleccion_volver = 'x'
    
    while eleccion_volver.lower() != 'v':
        eleccion_volver = input('Ingresa "v" para volver al menu: ')

finalizar = False

while not finalizar:
    # Mostrar menu inicio
    menu = inicio()

    match menu:
        case 1:
            mis_categorias = mostrar_categorias(ruta)
            mi_categoria = elegir_categorias(mis_categorias)
            mis_recetas = mostrar_recetas(mi_categoria)
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
            volver_inicio()
            pass
        case 2:
            mis_categorias = mostrar_categorias(ruta)
            mi_categoria = elegir_categorias(mis_categorias)
            crear_receta(mi_categoria)
            volver_inicio()
            pass
        case 3:
            crear_categoria(ruta)
            volver_inicio()
            pass
        case 4:
            mis_categorias = mostrar_categorias(ruta)
            mi_categoria = elegir_categorias(mis_categorias)
            mis_recetas = mostrar_recetas(mi_categoria)
            mi_receta = elegir_receta(mis_recetas)
            eliminar_receta(mi_receta)
            volver_inicio()
            pass
        case 5:
            mis_categorias = mostrar_categorias(ruta)
            mi_categoria = elegir_categorias(mis_categorias)
            eliminar_categoria(mi_categoria)
            volver_inicio()
            pass
        case 6:
            finalizar = True