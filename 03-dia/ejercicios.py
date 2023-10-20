# Ejercicios 1
palabra = 'ordenador'
print(palabra[4])

frase = 'En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son.'
print(frase.index('práctica', 35))

# Ejercicios 2
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

print(frase[::-1])

# Ejercicios 3
lista_palabras = ['me', 'gusta', 'programar']
print(' '.join(lista_palabras))

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("difícil", "fácil")
resultado = resultado.replace("mala", "buena")
print(resultado)

# Ejercicios 4
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(frutas)
print(eliminado)

# Ejercicios 5
mi_dic = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista"
}
print(mi_dic)

mi_dict = {
    "valores": {"v1": 3, "v2": 6},
    "puntos": {
        "points1": 9,
        "points2": [10, 300, 15]
    }
}
print(mi_dict["puntos"]["points2"][1])

# Ejercicios 6
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(mi_lista)

# Ejercicio 7
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo)
sorteo.pop()
print(sorteo)

# Ejercicio 8
print(17834 / 34 > 87 * 56)
print(25 ** 0.5 == 5)