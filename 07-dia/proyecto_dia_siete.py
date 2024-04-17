class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
    
class Cliente(Persona):
    def __init__(self, nombre, apellido, balance) -> None:
        super().__init__(nombre, apellido)
        self.balance = balance
        
    def __str__(self) -> str:
        return f'Cliente: {self.nombre} {self.apellido}, balance: {self.balance}'
    
    def depositar(self):
        print('Cuanto dinero vas a depositar? ')
        dinero = int(input())
        self.balance += dinero
           
    def retirar(self):
        print('Cuanto dinero vas a retirar? ')
        dinero = int(input())
        self.balance -= dinero
        

def crear_cliente() -> Cliente:
    print('Crear cliente')
    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')
    balance = int(input('Ingresa tu dinero: '))
    return Cliente(nombre, apellido, balance)
        

def inicio():
    cliente = crear_cliente()
    option = 'x'
    while option != 3:
        print('''
              Elije una opcion:
              1) Depositar
              2) Retirar
              3) Salir
              ''')
        
        option = int(input())
        
        match option:
            case 1:
                print('Depositar dinero!')
                cliente.depositar()
                print(cliente)
            case 2:
                print('Retirar dinero!')
                cliente.retirar()
                print(cliente)
            case 3:
                print('Saliste del programa!')
                print(cliente)
                

if __name__ == '__main__':
    inicio()