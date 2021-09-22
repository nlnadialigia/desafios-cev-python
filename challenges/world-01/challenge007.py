color = '\33[1;35m'
clear = '\33[0;0m'
grade1 = float(input('Insira a primeira nota: '))
grade2 = float(input('Insira a segunda nota: '))

print(color)
print('Minha Resolução: ', end='')
print(clear)
avarage = (grade1 + grade2)/2
print('Suas notas são {} e {}. A média de suas notas é {}' .format(grade1, grade2, avarage))


