nombres = ["Ana", "Jose", "Judy"]
edades = [34, 43, 21]
ciudades = ["Lima", "Mexico", "Argentina", "Chile"]
combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")
