from collections import Counter, defaultdict


numbers = [4, 7, 5, 6, 4, 23, 7, 43, 2, 5]
print(Counter(numbers))

print(Counter('paragacutirimicuaro'))

palabra = 'Del techo blanco al hoyo prestas'
print(Counter(palabra.split()))

serie = Counter([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
print(serie.most_common())
print(serie.most_common(3))
print(list(serie))

mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
print(mi_dic['dos'])

mi_dic2 = defaultdict(lambda: 'nada')
mi_dic2['uno'] = 'verde'
print(mi_dic2['uno'])
print(mi_dic2['dos'])
print(mi_dic2)
