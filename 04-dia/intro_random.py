from random import *

# numero entero aleatorio a partir del rango
numero = randint(1, 50)
print(numero)

# uniform lanza un valor aleatorio desde el rango
# le ponemos la cantidad de decimales que queremos con round
numero = round(uniform(1, 50), 2)
print(numero)

# nos da un numero aleatorio con decimales
numero = random()
print(numero)

# choice trabaja con cualquier tipo de coleccion
colores = ["azul", "rojo", "verde", "amarillo", "cafe"]
print(choice(colores))

# shuffle hace una mezcla
# creamos una lista que va de cierto rango en cierto numero
numeros = list(range(5, 50, 5))
# mezclamos la lista
shuffle(numeros)
print(numeros)

al = randint(1, 10)
print(al)