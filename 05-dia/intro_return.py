def multiplicar(numero1: int, numero2: int):
    return numero1 * numero2


resultado = multiplicar(7, 8)
print(resultado)


def invertir_palabra(palabra):
    return ''.join(reversed(palabra.upper()))


print(invertir_palabra("Python"))

def potencia(num_1, num_2):
    return num_1 ** num_2


print(potencia(4,33))


def dolares_euros(dolar):
    return dolar * 0.90


print(dolares_euros(100))