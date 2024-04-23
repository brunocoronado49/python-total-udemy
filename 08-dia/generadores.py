"""
Los generadores son un tipo especial de function
que en vez de devolvernos un valor terminado
va produciendo el valor a medida que lo vamos usando
en vez de return se usa yield
"""


# function normal
def normal_function():
    return 4


def function_generator():
    yield 4


print(normal_function())
print(function_generator())

generado = function_generator()
# con next se le indica que produzca el generador
print(next(generado))


def lista_normal():
    lista = []
    for numero in range(1, 5):
        lista.append(numero * 7)
    return lista


def lista_generada():
    for numero in range(1, 5):
        yield numero * 7


print(lista_normal())
print(lista_generada())
mi_lista_generada = lista_generada()
print(next(mi_lista_generada))
print(next(mi_lista_generada))
print(next(mi_lista_generada))

# Ejercicios


def infinite_numbers():
    numero = 0
    while True:
        numero += 1
        yield numero


generador = infinite_numbers()


def multiples():
    resultado = 0
    numero_natural = 1
    while True:
        resultado = 7 * numero_natural
        numero_natural += 1
        yield resultado


def juego():
    vidas = 'Te quedan 3 vidas'
    yield vidas
    vidas = 'Te quedan 2 vidas'
    yield vidas
    vidas = 'Te queda 1 vida'
    yield vidas
    vidas = 'Game Over'
    yield vidas