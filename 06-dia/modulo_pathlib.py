from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/franc/Developer/Cursos/python-total-udemy/textos/otro_archivo.txt')

# Convierte la ruta a una de windows
ruta_win = PureWindowsPath(carpeta)
print(ruta_win)

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if carpeta.exists():
    print('Existe el archivo')
else:
    print('No existe el archivo')