# Ejercicios de practica

def abrir_leer(file):
    archivo = open(file)
    return archivo.read()


def sobreescribir(file):
    archivo = open(file, 'w')
    archivo.write('contenido eliminado')
    

def registro_error(file):
    archivo = open(file, 'a')
    archivo.write('se ha registrado un error de ejecución')
    archivo.close()