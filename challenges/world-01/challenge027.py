color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
name = str(input('Nome completo: '))
list = name.split()
n = len(list)

print('Primeiro nome: {}'.format(list[0]))
print('Último nome: {}'.format(list[n-1]))
