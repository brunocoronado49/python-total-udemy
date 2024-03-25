my_file = open('text.txt', 'w')
my_file.write('soy nuevo en esto')
my_file.close()

my_new_file = open('text1.txt', 'a')
my_new_file.write('hola de nuevo\n')
my_new_file.write('esta linea es la ultima\n')
# my_new_file.writelines(['hola', 'mundo', 'bruce'])

my_list = ['perros', 'juegos', 'python']

for p in my_list:
    my_new_file.writelines(p + '\n')

my_new_file.close()

# Ejercicios
mi_archivo = open('mi_archivo.txt', 'w')
mi_archivo.write('Nuevo texto')
mi_archivo.close()
mi_archivo = open('mi_archivo.txt')
print(mi_archivo.read())

mi_archivo = open('mi_archivo.txt', 'a')
mi_archivo.write("Nuevo inicio de sesión")
mi_archivo.close()
mi_archivo = open('mi_archivo.txt', 'r')
print(mi_archivo.read())

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
registro = open('registro.txt', 'a')
for l in registro_ultima_sesion:
    registro.writelines(l + '\t')
registro.close()
registro = open('registro.txt', 'r')
print(registro.read())