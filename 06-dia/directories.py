import os
from pathlib import Path

carpeta = Path('C:/Users/franc/Developer/Cursos/python-total-udemy/textos')
archivo = carpeta/'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

ruta = 'C:\\Users\\franc\\Developer\\Cursos\\python-total-udemy\\textos\\otro_archivo.txt'
print(os.path.basename(ruta))


# ruta = os.getcwd()
# print(ruta)

# ruta = os.chdir('C:\\Users\\franc\\Developer\\Cursos\\python-total-udemy\\textos')

# archivo = open('otro_archivo.txt', 'w')
# archivo.write('Este archivo esta en otra ruta')
# archivo.close()

# archivo = open('otro_archivo.txt', 'r')
# print(archivo.read())
# print(ruta)

# archivo.close()

# permite crear nuevas rutas
# ruta = os.makedirs('C:\\Users\\franc\\Developer\\Cursos\\python-total-udemy\\otra')

# ruta = 'C:\\Users\\franc\\Developer\\Cursos\\python-total-udemy\\otra\\texto.txt'

# elemento = os.path.basename(ruta)
# elemento = os.path.dirname(ruta)
# elemento = os.path.split(ruta)
# print(elemento)

# eliminar directorio
# os.rmdir('C:\\Users\\franc\\Developer\\Cursos\\python-total-udemy\\textos')


# otro = open('C:\\Users\\franc\\Developer\\Cursos\\python-total-udemy\\textos\\otro_archivo.txt')

# print(otro.read())