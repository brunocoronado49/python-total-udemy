mi_texto = "Esta es una prueba"

resultado = mi_texto[8]
print(resultado)

otro_resultado = mi_texto.index("n")
print(otro_resultado)
otro_resultado = mi_texto.index("a", 5)
print(otro_resultado)

# busca de derecha a izquierda
metodo_rindex = mi_texto.rindex("a")
print(metodo_rindex)