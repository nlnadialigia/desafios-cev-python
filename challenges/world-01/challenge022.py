color = '\33[1;35m'
clear = '\33[0;0m'
name = str(input('Nome completo: '))

print(color)
print('Minha Resolução: ', end='')
print(clear)


print('Maiúscula: {}' .format(name.upper()))
print('Minúscula: {}' .format(name.lower()))

space = name.count(' ')
nameWithoutSpace = len(name) - space

print('Total das letras sem espaço: {}' .format(nameWithoutSpace))

nameList = name.split()
print('Letras do primeiro nome: {}' .format(len(nameList[0])))
