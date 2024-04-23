"""
Módulo principal
para el desarrollo del programa por turnos
"""


import numeros_proyecto


def preguntar():
    print('Bienvenido a Farmacia Pyton')

    while True:
        print('''
        Chose an option:
        1) Perfumery
        2) Drugstore
        3) Cosmetics
        ''')

        try:
            mi_rubro = int(input('Elige tu rubro:'))
            [1, 2, 3].index(mi_rubro)
        except ValueError:
            print('Esa no es una option valid')
        else:
            break

    numeros_proyecto.decorador(mi_rubro)


def inicio():
    while True:
        preguntar()
        try:
            nuevo_turno = input('Quieres tomar otro turno? S/N: ').upper()
            ['S', 'N'].index(nuevo_turno)
        except ValueError:
            print('Esa no es una option valid')
        else:
            if nuevo_turno == 'N':
                print('Gracias por tu cita')
                break


inicio()
