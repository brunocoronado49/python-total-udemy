def multiplicar(numero1, numero2):
    return numero1 * numero2


resultado = multiplicar(7, 8)
print(resultado)


def invertir_palabra(palabra):
    return ''.join(reversed(palabra.upper()))


palabra = "Python"
print(invertir_palabra(palabra))