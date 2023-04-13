def suma(**kwargs):
    print(type(kwargs))
    

suma(x = 3, y = 5, z = 2)


def suma_nueva(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    print(f"la suma de los valores es {total}")
        
        
suma_nueva(x = 3, y = 5, z = 2)
