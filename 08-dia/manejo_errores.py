def suma():
    try:
        n1 = int(input('Ingresa un numero: '))
        n2 = int(input('Ingresa otro numero: '))
        print(n1 + n2)
    except TypeError:
        print('No puedes concatenar dos tipos diferentes')
    except ValueError:
        print('Ese no es un numero')
    else:
        print('Muy bien, si supiste que sumar')
    finally:
        print('Eso es todo')


suma()


def pedir_numero():
    while True:
        try:
            numero = int(input('Ingresa un numero: '))
        except TypeError:
            print('Ese no es un numero')
        else:
            print(f'El numero es: {numero}')
            break
    print('Gracias')


pedir_numero()


# Ejercicios

def suma(num1, num2):
    try:
        resultado = num1 + num2
    except TypeError:
        print('Error inesperado')
    else:
        print(resultado)


# Ejercicios

def cociente(num1, num2):
    try:
        resultado = num1 / num2
    except TypeError:
        print('Los argumentos a ingresar deben ser números')
    except ZeroDivisionError:
        print('El segundo argumento no debe ser cero')
    else:
        print(resultado)


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print('El archivo no fue encontrado')
    except:
        print('Error desconocido')
    else:
        print('Abriendo exitosamente')
    finally:
        print('Finalizando ejecucion')
