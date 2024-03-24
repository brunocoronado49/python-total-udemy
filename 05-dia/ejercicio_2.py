def lista_palabra(palabra):
    lista_nueva = []
    lista_vieja = list(''.join(palabra))
    
    for i in lista_vieja:
        if i not in lista_nueva:
            lista_nueva.append(i)
            
    return lista_nueva


print(lista_palabra('marianami'))