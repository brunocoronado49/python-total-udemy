lista = ["a", "b", "c", "d"]
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

mi_lista = ["Bruce", "Maria", "John", "Franco", "Bruno", "Berna"]
for name in mi_lista:
    if name.startswith("B"):
        print(f"Hola {name}!")
    else:
        print(f"Saludos {name}")

numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor += numero
print(mi_valor)

palabra = "Python"
for letra in palabra:
    print(letra)

for palabra in "chanchito feliz":
    print(palabra)

for obj in [[1,2], [3,4], [5,6]]:
    print(obj)

for a, b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

dic = {
    "clave_uno": 1,
    "clave_dos": 2,
    "clave_tres": 3
}
for item in dic:
    print(item)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for a, b in dic.items():
    print(a, b)