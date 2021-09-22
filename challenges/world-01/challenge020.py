from random import shuffle
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

students = input('Nome dos alunos: ')
order = students.split()
shuffle(order)
print('A ordem para apresentação dos trabalhos é: {}' .format(order))
