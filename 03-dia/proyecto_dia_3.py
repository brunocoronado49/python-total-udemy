# Inputs del usuario
poema = input("Ingresa un texto: ")
print(poema)

letras = []
poema = poema.lower()

letras.append(input("Ingresa una letra al azar: ").lower())
letras.append(input("Ingresa otra letra al azar: ").lower())
letras.append(input("Ingresa una ultima letra al azar: ").lower())

print("\n")
print("CANTIDAD DE LETRAS: ")
cant_letras1 = poema.count(letras[0])
cant_letras2 = poema.count(letras[1])
cant_letras3 = poema.count(letras[2])

print(f"Se encontraron {cant_letras1} veces la letra '{letras[0]}'")
print(f"Se encontraron {cant_letras2} veces la letra '{letras[1]}'")
print(f"Se encontraron {cant_letras3} veces la letra '{letras[2]}'")

print("\n")
print("CANTIDAD DE PALABRAS: ")
palabras = poema.split()
cant_palabras = len(palabras)
print(f"Se encontraron {cant_palabras} palabras en el texto")

print("\n")
print("LETRAS DE INCIO Y FIN: ")
letra_inicio = poema[0]
letra_final = poema[-1]
print(f"la letra inicial es {letra_inicio} y la letra final es {letra_final}")

print("\n")
print("TEXTO  INVERTIDO: ")
palabras.reverse()
poema_invertido = " ".join(palabras)
print(f"Texto invertido: '{poema_invertido}'")

print("\n")
print("PYTHON EN EL TEXTO: ")
buscar_python = "python" in poema
dic = {"si": True, "no": False}
print(f"La palabra 'python' {dic[buscar_python]} se encuentra en el texto")