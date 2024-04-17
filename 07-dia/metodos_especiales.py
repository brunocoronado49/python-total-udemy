mi_lista = [1, 1, 1, 1, 1, 1, 1]
print(mi_lista)

class Objeto:
    pass


mi_obj = Objeto()
print(mi_obj)


class CD:
    def __init__(self, autor, titulo, canciones) -> None:
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
        
    def __str__(self) -> str:
        return f'Album {self.titulo} de {self.autor} con {self.canciones} rolitas'
    
    def __len__(self) -> int:
        return self.canciones
    
    def __del__(self):
        print('Se ha eliminado el objeto')
        
        
mi_cd = CD('Megadeth', 'Peace Sells', 12)
print(mi_cd)
print(len(mi_cd))

# Eliminar instancias
del mi_cd


# Ejercicios

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self) -> str:
        return f'"{self.titulo}", de {self.autor}'
    
    def __len__(self) -> int:
        return self.cantidad_paginas
    
    def __del__(self):
        print('Libro eliminado')