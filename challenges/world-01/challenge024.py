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



