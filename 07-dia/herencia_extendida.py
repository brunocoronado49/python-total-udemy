class Animal:
    def __init__(self, edad, color) -> None:
        self.edad = edad
        self.color = color
        
    def nacer(self):
        print('Este animal ha nacido')
        
    def hablar(self):
        print('Este animal emite un sonido')
        

class Ave(Animal):
    def __init__(self, edad, color, altura_vuelo) -> None:
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
    
    def hablar(self):
        print('pio')
        
    def volar(self, metros):
        print(f'el ave vuela {metros} metros')


mi_animal = Animal(5, 'cafe')

piolin = Ave(3, 'amarillo', 30)
piolin.nacer()
piolin.hablar()
piolin.volar(100)


class Padre:
    def hablar(self):
        print('Hola!')


class Madre:
    def reir(self):
        print('jajaja')
    
    def hablar(self):
        print('Que tal!')


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()

print(Nieto.__mro__)