color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
name = str(input('Nome completo: '))
print('Seu nome tem Silva? {}'.format('Silva' in name.title()))
