class Ave:
    alas = True
    
    def __init__(self, color, especie) -> None:
        self.color = color
        self.especie = especie
        
    # Metodos de instancia
    def piar(self):
        print(f'Pio, mi color es {self.color}')
        
    def volar(self, metros):
        print(f'El ave volo {metros} metros')
        self.piar()
        
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajarraco es {self.color}')
        
    # Metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Ave.alas)
        
    # Metodos estaticos
    @staticmethod
    def mirar():
        print('El ave mira las flores')
        
    
piolin = Ave('amarillo', 'canario')
piolin.pintar_negro()
piolin.volar(50)
piolin.alas = False

Ave.poner_huevos(3)

Ave.mirar()


# Ejercicios

class Mascota:    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def respirar():
        print('Inhalar... Exhalar')
        
        
Mascota.respirar()


class Jugador:
    vivo = False
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(cls.vivo)
        
        
Jugador.revivir()


class Personaje:
    def __init__(self, cantidad_flechas) -> None:
        self.cantidad_flechas = cantidad_flechas
        
    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
        print(self.cantidad_flechas)
        

personaje = Personaje(10)
personaje.lanzar_flechas()