class Vaca:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
    def hablar(self):
        print(f'{self.nombre} dice muuu!')
        

class Oveja:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
    def hablar(self):
        print(f'{self.nombre} dice beee!')
        
        
vaca1 = Vaca('lola')
obeja = Oveja('nube')


def animal_habla(animal):
    animal.hablar()
    
animal_habla(vaca1)
animal_habla(obeja)

# animales = [vaca1, obeja]

# for animal in animales:
#     animal.hablar()


# Ejercicios

class Mago():
    def atacar(self):
        print("Ataque mágico")
        
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")
        
    def defender(self):
        print("Esconderse")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
    def defender(self):
        print("Bloqueo")
        

arquero = Arquero()
mago = Mago()
samurai = Samurai()

personajes = [arquero, mago, samurai]

for personaje in personajes:
    personaje.atacar()
    
def personaje_defender(pesonaje):
    pesonaje.defender()
    
personaje_defender(arquero)
personaje_defender(mago)
personaje_defender(samurai)