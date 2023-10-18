def devolver_distintos(numero_uno, numero_dos, numero_tres):
    suma = numero_uno + numero_dos + numero_tres
    lista_numeros = [numero_uno, numero_dos, numero_tres]
    if suma > 15:
        return max(lista_numeros)
    elif suma < 10:
        return min(lista_numeros)
    else:
        lista_numeros.sort()
        return lista_numeros[1]


print(devolver_distintos(2, 4, 6))
print(devolver_distintos(8, 6, 12))
