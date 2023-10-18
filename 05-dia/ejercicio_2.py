def letras_en_palabras(palabra):
    lista_nueva = []
    lista = list(''.join(palabra))

    for letra in lista:
        if letra not in lista_nueva:
            lista_nueva.append(letra)
    return lista_nueva


print(letras_en_palabras("parangacutirimicuaro"))
