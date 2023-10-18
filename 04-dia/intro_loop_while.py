monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("Chale wey ando bien jodido")

respuesta = "s"
while respuesta == "s":
    respuesta = input("Quieres seguir? s/n")
else:
    print("Gracias")

while respuesta == "s":
    pass

nombre = input("Tu nombre ")
for letra in nombre:
    if letra == "r":
        continue
        # break
    print(letra)

numero = 10
while numero <= 10:
    numero -= 1
    print(numero)
