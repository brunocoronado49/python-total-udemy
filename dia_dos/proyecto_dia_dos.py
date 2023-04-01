nombre = input("Dime tu nombre: ")
ventas = float(input("Cuales fueron tus ventas: "))
comision = round(ventas * 13 / 100, 2)

print(f"Ok {nombre}. Este mes ganaste ${comision}")