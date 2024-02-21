def checar_cifras(numero):
    return numero in range(100, 1000)


print(checar_cifras(657))


def checar_lista(lista):
    valores = []
    for numero in lista:
        if numero in range(100, 1000):
            valores.append(numero)
        else:
            pass
    return valores


resultado_lista = checar_lista([103, 2170, 30, 100])
print(resultado_lista)


def positive_numbers(list_nums):
    for num in list_nums:
        if num < 0:
            return False
    
    return True

print(positive_numbers([1, 2, 3, 4, 5, -1, 2, -5]))


def sum_numbers(list_nums):
    sum = 0
    for num in list_nums:
        if num > 0 and num < 1000:
            sum += num
    
    return sum


print(sum_numbers([2, 3, 6, 500, 877, 321, 10]))