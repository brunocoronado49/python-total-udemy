def suma_cuadrados(*args):
    total = 0
    
    for arg in args:
        total += arg * arg
    
    return total


print(suma_cuadrados(2, 4, 6))


def suma_absolutos(*args):
    total = 0
    
    for i in args:
        total += abs(i)
        
    return total


print(suma_absolutos(3.4, -2, 41))


def suma_persona(nombre, *args):
    total = 0
    
    for i in args:
        total += i
    
    return f'Hola {nombre}, el total es {total}'


print(suma_persona('Bruce', 2, 4, 6))