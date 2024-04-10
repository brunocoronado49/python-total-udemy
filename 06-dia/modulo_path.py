from pathlib import Path


base = Path.home()
guia = Path(base, 'America', 'Mexico', Path('Zacatecas', 'El_Saladillo.txt'))
#guia2 = guia.with_name('un_parque.txt')
#print(guia2)
print(guia.parent)

# Para enumerar todos los archivos txt
guia_nueva = Path(Path.home(), 'America')
for txt in Path(guia_nueva).glob('**/*.txt'):
    print(txt)
    
guia_relativa = Path('America', 'Mexico', 'Zacatecas', 'El_Saladillo.txt')
en_america = guia_relativa.relative_to(Path('America'))
en_mexico = guia_relativa.relative_to(Path('America', 'Mexico'))

print(en_america)
print(en_mexico)