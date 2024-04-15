class Ave:
    alas = True
    
    def __init__(self, color, especie) -> None:
        self.color = color
        self.especie = especie
        
    def piar(self):
        print(f'Pio, mi color es {self.color}')
        
    def volar(self, metros):
        print(f'El ave volo {metros} metros')
        
    
piolin = Ave('amarillo', 'canario')
piolin.piar()
piolin.volar(20)


# Ejercicios

class Perro:
    def __init__(self) -> None:
        pass
    
    def ladrar(self):
        print('Guau!')
        

class Mago:
    def __init__(self) -> None:
        pass
    
    def lanzar_hechizo(self):
        print('¡Abracadabra!')
        

merlin = Mago()
merlin.lanzar_hechizo()


class Alarma:
    def __init__(self) -> None:
        pass
    
    def postergar(self, cantidad_minutos):
        print(f'La alarma ha sido pospuesta {cantidad_minutos} minutos')
        

alarma = Alarma()
alarma.postergar(5)