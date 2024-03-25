my_file = open('text.txt')

print(my_file.read())
print('===========')
print(my_file.readline().upper())
print('===========')
print(my_file.readlines())
print('===========')
for line in my_file:
    print(f'Aqui dice: {line}')
print('===========')

my_file.close()