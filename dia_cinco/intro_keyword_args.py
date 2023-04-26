def suma(**kwargs):
    print(type(kwargs))


suma(x=3, y=5, z=2)


def suma_nueva(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    print(f"la suma de los valores es {total}")


suma_nueva(x=3, y=5, z=2)


def prueba_varios(a, b, *args, **kwargs):
    print(f"numero uno {a}")
    print(f"numero dos {b}")

    for arg in args:
        print(f"esto es un arg: {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


prueba_varios(10, 20, 45, 60, 74, x="uno", y="dos")

args = [45, 60, 74]
kwargs = {"x": "uno", "y": "dos"}
prueba_varios(10, 20, *args, **kwargs)
