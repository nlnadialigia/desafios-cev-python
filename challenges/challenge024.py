color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
city = str(input('Qual o nome da cidade? '))
name = city.strip().split()
first = name[0]

print(name)
print(first)
print('Santo' in first)

print(color)
print('Resolução do Professor: ', end='')
print(clear)
city = str(input('Em que cidade você nasceu? ')).strip()
name = city[:5].title()
print(name)
print('Santo' in name)


