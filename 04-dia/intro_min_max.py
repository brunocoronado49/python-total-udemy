menor = min(58, 96, 72, 64, 32, 10)
mayor = max([58, 96, 72, 64, 32, 10])
print(menor)
print(mayor)

lista = list(range(13, 32, 2))
print(min(lista))
print(max(lista))

# Primero en orden alfabetico y ultimo en el mismo orden
nombres = ["juan", "pablo", "alicia", "carlos"]
print(min(nombres))
print(max(nombres))

# Igual que el anterior pero busca primero en mayusculas
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

new_list = [2*5, 4//3, 6+7, 8-2, 10**4]
print(min(new_list))
print(max(new_list))


