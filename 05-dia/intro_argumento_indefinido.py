def suma(a, b):
    return a + b


print(suma(5, 6))


def otra_suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def otra_suma_simple(*args):
    return sum(args)


print(otra_suma(5, 6, 34, 64, 42))
print(otra_suma_simple(5, 6, 34, 64, 42))