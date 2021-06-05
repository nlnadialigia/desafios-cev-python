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

print(color)
print('Resolução do Professor: ', end='')
print(clear)

print('Maiúscula: {}' .format(name.upper()))
print('Minúscula: {}' .format(name.lower()))
print('Total das letras sem espaço: {}' .format(len(name) - name.count(' ')))
print('Letras do primeiro nome: {}' .format(name.find(' ')))

separa = name.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

