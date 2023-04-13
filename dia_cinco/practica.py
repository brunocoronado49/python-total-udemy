import random

def reducir_lista(lista_numeros):
    lista_nueva = []
    for numero in lista_numeros:
        if numero not in lista_nueva:
            lista_nueva.append(numero)
    mayor = max(lista_nueva)
    lista_nueva.remove(mayor)
    return lista_nueva


lista = [1,2,15,7,2]

resultado = reducir_lista(lista)
#print(resultado)

lista_carrera = ["Ciencia de datos", "backend", " iOS Dev"]
print(f"Tu carrera sera: {random.choice(lista_carrera)}")