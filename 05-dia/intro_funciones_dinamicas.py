def checar_cifras(numero):
    return numero in range(100, 1000)


resultado = checar_cifras(657)
print(resultado)


def checar_lista(lista):
    valores = []
    for numero in lista:
        if numero in range(100, 1000):
            valores.append(numero)
        else:
            pass
    return valores


resultado_lista = checar_lista([103, 2170, 30, 100])
print(resultado_lista)
