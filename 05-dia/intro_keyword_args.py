def suma(**kwargs):
    print(type(kwargs))
    

suma(x = 3, y = 5, z = 8)


def suma_nueva(**kwargs):
    total = 0
    
    for c, v in kwargs.items():
        print(f'{c} + {v}')
        total += v
    
    print(f'Total: {total}')


suma_nueva(x = 3, y = 5, z = 8)


def probar_varios(a, b, *args, **kwargs):
    print(f'Num 1: {a}')
    print(f'Num 2: {b}')
    
    for i in args:
        print(f'args: {i}')
        
    for c,v in kwargs.items():
        print(f'clave: {c} - valor: {v}')


probar_varios(10, 20, 45, 60, 74, x = "uno", y = "dos")

args = [75, 110, 94]
kwargs = {"x": "equis", "y": "ye"}
probar_varios(1, 2, *args, **kwargs)
