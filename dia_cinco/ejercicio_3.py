def ceros_vecinos(*args):
    contador = 0
    for n in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1

    return False


print(ceros_vecinos(2, 4, 5, 3, 4, 6, 7, 4, 3, 2, 3, 4, 9, 6))
print(ceros_vecinos(2, 4, 5, 3, 4, 6, 7, 0, 0, 2, 3, 4, 9, 6))
