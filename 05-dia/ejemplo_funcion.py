precios_cafe = [("capuccino", 1.5), ("expresso", 2.8), ("Moka", 1.9)]

for cafe, precio in precios_cafe:
    print(cafe, precio)


def cafe_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)


print(cafe_caro(precios_cafe))

cafe, precio = cafe_caro(precios_cafe)
print(f"El cafe mas caro es el {cafe} con un precio de {precio}")