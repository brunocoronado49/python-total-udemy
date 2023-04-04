mi_diccionario = {
    "c1": "valor1",
    "c2": "valor2",
    "c3": "valor3",
}
print(type(mi_diccionario))
print(mi_diccionario)
resultado = mi_diccionario["c1"]
print(resultado)

cliente = {
    "nombre": "Juan",
    "apellido": "Fuentes",
    "peso": 72,
    "talla": 1.76
}
consulta = (cliente["apellido"])
print(consulta)

dic = {
    "c1": 55,
    "c2": [10,20,30],
    "c3": {
        "s1": 100,
        "s2": 200
    }
}
print(dic["c2"])
print(dic["c2"][1])
print(dic["c3"])
print(dic["c3"]["s2"])

mi_dict = {
    "c1": ["a", "b", "c"],
    "c2": ["d", "e", "f"]
}
print(mi_dict["c2"][1].upper())
print(mi_dict["c1"][0].upper())

otro_dic = {
    "c1": "a",
    "c2": "b"
}
print(otro_dic)
otro_dic["c3"] = "c"
print(otro_dic)

otro_dic["c2"] = "BBBB"
print(otro_dic)

print(otro_dic.keys())
print(otro_dic.values())
print(otro_dic.items())