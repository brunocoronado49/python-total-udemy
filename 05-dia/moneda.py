from random import choice


def lanzar_moneda():
    moneda = ['cara', 'cruz']
    cara = choice(moneda)
    return cara


def suerte(resultado, lista):
    if resultado == 'cara':
        print('La lista se eliminara')
        lista.clear()
        print(f'lista: {lista}')
    elif resultado == 'cruz':
        print('La lista se salvo')
        print(lista)
        

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
moneda = lanzar_moneda()
print(moneda)
suerte(moneda, lista)