def kwargs_len(**kwargs):
    return len(kwargs)


print(kwargs_len(a = 10, b = 20, c = 30))


def lista_attrs(**kwargs):
    return [list(kwargs.keys()), list(kwargs.values())]

print(lista_attrs(a = 10, b = 20, c = 30))


def marca_persona(nombre, **kwargs):
    print(f'Hola {nombre}')
    for c,v in kwargs.items():
        print(f'{c} = {v}')
        
        
marca_persona('Lizbeth', ojos = 'Cafes', cabello = 'Castanio')