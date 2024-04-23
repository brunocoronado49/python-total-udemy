"""
Functions to generate the tickets in each
store of the drugstore
"""


def number_generate_perfumery():
    for num in range(1, 100):
        yield f'P-{num}'


def number_generate_drugstore():
    for num in range(1, 100):
        yield f'F-{num}'


def number_generate_cosmetics():
    for num in range(1, 100):
        yield f'C-{num}'


p = number_generate_perfumery()
f = number_generate_drugstore()
c = number_generate_cosmetics()


def decorador(rubro):
    print('*' * 23 + '\n')
    print('Su numero es:')

    if rubro == 1:
        print(next(p))
    elif rubro == 2:
        print(next(f))
    elif rubro == 3:
        print(next(c))
    else:
        print('Option not valid')
    print('Espera para tu turno')
    print('*' * 23 + '\n')
