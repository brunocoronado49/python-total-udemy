from random import *

numero = randint(1, 51)
print(numero)

# con decimal
numero = round(uniform(1, 50), 2)
print(numero)

numero = random()
print(numero)

colores = ["azul", "rojo", "verde", "amarillo", "cafe"]
print(choice(colores))

numeros = list(range(5, 50, 5))
shuffle(numeros)
print(numeros)