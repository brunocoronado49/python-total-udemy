# Utilizar la documentacion oficial de pycharm y de python
dic = { "c1": 100, "c2": 500 }

print(dic)

s = dic.popitem()
print(s)
print(dic)

txt = ",:_#,,,,,,:::____##Pyton_ _Total,,,,,,::#".lstrip(",:_#%")
print(txt)

fruits = ['mango', 'banana', 'cereza', 'ciruela', 'pomelo']

# Inserta en el indice, la fruta
fruits.insert(2, 'naranja')
print(fruits)

# Elementos en comun de sets
marcas_sm = {"Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung"}
aisladors = marcas_sm.isdisjoint(marcas_tv)
print(aisladors)