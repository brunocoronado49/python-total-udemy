my_file = open('text.txt', 'w')
my_file.write('soy nuevo en esto')
my_file.close()

my_new_file = open('text1.txt', 'a')
my_new_file.write('hola de nuevo\n')
my_new_file.write('esta linea es la ultima\n')
# my_new_file.writelines(['hola', 'mundo', 'bruce'])

my_list = ['perros', 'juegos', 'python']

for p in my_list:
    my_new_file.writelines(p + '\n')

my_new_file.close()