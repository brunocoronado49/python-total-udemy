class Animal:
    def __init__(self, edad, color) -> None:
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print('Este animal ha nacido')
    

class Perro(Animal):
    def __init__(self) -> None:
        super().__init__()
        
    
seven = Animal(3, 'cafe')
seven.nacer()
print(seven.color, seven.edad)


# Revisar de donde heredan y a cuales heredan
print(Perro.__bases__)
print(Animal.__subclasses__())


# Ejercicios

class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        

class Alumno(Persona):
    def __init__(self, nombre, edad) -> None:
        super().__init__(nombre, edad)
        

class Mascota:
    def __init__(self, nombre, edad, cantidad_patas) -> None:
        self.nombre = nombre
        self.edad = edad
        self.cantidad_patas = cantidad_patas
        

class Perro(Mascota):
    def __init__(self, nombre, edad, cantidad_patas) -> None:
        super().__init__(nombre, edad, cantidad_patas)
        
        
class Vehiculo:
    def __init__(self) -> None:
        pass
    
    def acelerar(self):
        pass
    
    def frenar(self):
        pass
    

class Automovil(Vehiculo):
    def __init__(self) -> None:
        super().__init__()
        
    def acelerar(self):
        return super().acelerar()
    
    def frenar(self):
        return super().frenar()