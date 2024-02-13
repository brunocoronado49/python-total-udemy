palabra = "Python"
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

# comprension de lista
# facilita el iterar cada elemento de la lista
# sustituye al for
palabra = "Videojuegos"
lista = [letra for letra in palabra]
print(lista)

lista = [letra for letra in "programacion"]
print(lista)

lista = [numero for numero in range(0, 21)]
print(lista)

lista = [numero / 2 for numero in range(0, 21, 2)]
print(lista)

lista = [numero for numero in range(0,31, 3) if numero * 2 > 10]
print(lista)

lista = [numero if numero * 2 > 10 else "no" for numero in range(0,31, 3)]
print(lista)

medidas = [10, 20, 30, 40, 50]
metros = [pies / 3.281 for pies in medidas]
print(metros)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(far - 32) * (5 / 9) for far in temperatura_fahrenheit]
print(grados_celsius)