"""
Los decoradores son funciones que modifican
el comportamiento de otras funciones
"""


def decorar_saludo(function):
    def otra_function(palabra):
        print('hola')
        function(palabra)
        print('adios')

    return otra_function


def new_upper(text):
    print(text.upper())


def new_lower(text):
    print(text.lower())


upper_decorada = decorar_saludo(new_upper)
upper_decorada('Python')


new_lower('Python')
# new_upper('Python')


def change_letters(tipo):
    def uppers(texto: str):
        print(texto.upper())

    def lowers(texto: str):
        print((texto.lower()))

    if tipo == 'may':
        return uppers
    elif tipo == 'min':
        return lowers


# operation = change_letters('may')
# operation('palabra')


# mi_function = uppers
# mi_function('Python')

# def una_function(function):
#     return function
#
# una_function(uppers('probando'))
