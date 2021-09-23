color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
total = 0
for c in range(0, 4):
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    gender = str(input('Sexo: '))
    total += age
avarage = total / 4

print('\33[1;34m*' * 40)
print('média de idade do grupo: {}'.format(avarage))
print('*' * 40)