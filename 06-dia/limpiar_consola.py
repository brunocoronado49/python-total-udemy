from os import system


# Como limpiar la consola
nombre = input('Dime tu nombre: ')
edad = int(input('Dime tu edad: '))

system('cls')

print(f'Tu nombre es {nombre} y tienes {edad} de edad')