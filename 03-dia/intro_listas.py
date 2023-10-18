mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
print(type(mi_lista))
print(mi_lista3)
mi_lista3.append("g")
print(mi_lista3)
mi_lista3[0] = "alfa"
print(mi_lista3)
mi_lista3.pop()
print(mi_lista3)
mi_lista3.pop(0)
print(mi_lista3)

otra_lista = ["hola", 55, 1.5]
print(len(otra_lista))
print(otra_lista[2])
print(otra_lista[0:2])

lista_ordenada = ["h", "d", "t", "b", "g", "a"]
lista_ordenada.sort()
print(lista_ordenada)
lista_ordenada.reverse()
print(lista_ordenada)