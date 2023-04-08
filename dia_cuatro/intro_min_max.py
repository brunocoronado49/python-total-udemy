menor = min(58, 96, 72, 64, 32, 10)
mayor = max(58, 96, 72, 64, 32, 10)
print(menor)
print(mayor)

lista = list(range(13, 32, 2))
print(min(lista))
print(max(lista))

nombres = ["juan", "pablo", "alicia", "carlos"]
print(min(nombres))
print(max(nombres))

nombre = "Brunista"
print(min(nombre).lower())
print(max(nombre).lower())

dic = {
    "c1": 34,
    "c2": 11
}
print(min(dic))
print(max(dic))
print(min(dic.values()))
print(max(dic.values()))