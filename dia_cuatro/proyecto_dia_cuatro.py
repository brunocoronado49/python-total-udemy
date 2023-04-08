from random import *

nombre = input("Dime tu nombre: ")
print(f"Hola {nombre}, bienvenido al juego 'Find the Number'")
numero_usuario = 0
intentos = 0
numero_correcto = randint(1, 100)

while numero_usuario != numero_correcto:
    numero_usuario = int(input("Ingresa un numero entre el 1 y el 100: "))
    intentos += 1
    if numero_usuario > numero_correcto:
        print("El numero ingresado es MAYOR al correcto, intentalo de nuevo")
    if numero_usuario < numero_correcto:
        print("El numero ingresado es MENOR al correcto, intentalo de nuevo")

print(f"Felicidades {nombre} el numero {numero_usuario} es el numero correcto!")
print(f"Cantidad de intentos: {intentos}")
