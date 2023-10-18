lista = ["A", "B", "C", "D"]
indice = 0
for item in lista:
    print(indice, item)
    indice += 1

# Recommendado
for indice, item in enumerate(lista):
    print(indice, item)

nueva_tuple = list(enumerate(lista))
print(nueva_tuple)
print(nueva_tuple[1][1])