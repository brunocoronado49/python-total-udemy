def reducir_lista(lista):
    lista_nueva = []
    
    for num in lista:
        if num not in lista_nueva:
            lista_nueva.append(num)
    
    numero_mayor = max(lista_nueva)
    lista_nueva.remove(numero_mayor)
    
    return lista_nueva


def promedio(lista):
    suma = 0
    
    for num in lista:
        suma += num
        promedio = suma / len(lista)
        
    return promedio


lista_numeros = [1, 2, 15, 7, 2, 8]
resultado_lista = reducir_lista(lista_numeros)
resultado_promedio = promedio(resultado_lista)
print(resultado_promedio)