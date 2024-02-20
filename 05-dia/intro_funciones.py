def saludo():
    '''
    esta funcion se encarga
    de retornar un saludo
    en pantalla
    '''
    return 'Hello World!'


print(saludo())


# con parametros
def saludar_persona(nombre):
    print(f"Hola {nombre}")


saludar_persona("Bruce")
saludar_persona("Franco")
saludar_persona("Cisco")

names = ['Juan', 'Lauren', 'Jenni']

for name in names:
    saludar_persona(name)
    
    
def number_cuadrado(number):
    print(number**2)
    
number_cuadrado(72)