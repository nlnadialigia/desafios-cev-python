from random import shuffle
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)

a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
students = [a, b, c, d]
shuffle(students)
print('A ordem para apresentação dos trabalhos é: ')
print(students)