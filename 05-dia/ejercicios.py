from random import randint


def lanzar_dados():
    valor_uno = randint(1, 6)
    valor_dos = randint(1, 6)
    
    return valor_uno, valor_dos


def evaluar_valor(valor_uno, valor_dos):
    suma = valor_uno + valor_dos
    
    if suma <= 6:
        return f'La suma es {suma}, triste.'
    elif suma > 6 and suma < 10:
        return f'la suma es {suma}, buena chance.'
    elif suma >= 10:
        return f'la suma es {suma}, buena jugada'
    

uno, dos = lanzar_dados()
print(uno, dos)
print(evaluar_valor(uno, dos))