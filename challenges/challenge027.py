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

print(color)
print('Resolução do Professor: ', end='')
print(clear)
n = str(input('Qual é seu nome completo? ')).strip()
name = n.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(name[0].title()))
print('Seu último nome é {}'.format(name[len(name)-1].title()))

