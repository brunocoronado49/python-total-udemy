class Ave:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        

tucan = Ave('Negro con blanco', 'Tucan')
print(f'Mi ave es un {tucan.especie} de color {tucan.color}')
print(tucan.alas)


# Ejercicios
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
        

casa_blanca = Casa('blanca', 4)


class Cubo:
    caras = 4
    def __init__(self, color):
        self.color = color
        

cubo_rojo = Cubo('rojo')


class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
        

harry_potter = Personaje('Humano', True, 17)