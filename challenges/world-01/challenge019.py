from random import choice
color = '\33[1;35m'
clear = '\33[0;0m'
a = input('Digite o aluno 01: ')
b = input('Digite o aluno 02: ')
c = input('Digite o aluno 03: ')
d = input('Digite o aluno 04: ')

print(color)
print('Minha Resolução: ', end='')
print(clear)
students = a, b, c, d
student = choice(students)
print('O aluno sorteado foi {}' .format(student))

