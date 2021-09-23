from datetime import date
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
year = date.today().year
adult = 0
young = 0
for c in range(0, 7):
    birth = int(input('Ano do nascimento: '))
    age = year - birth
    if age < 21:
        young += 1
    else:
        adult += 1
print('''
    Atingiram a MAIORIDADE: {}
    NÃO atingiram a MAIORIDADE: {}'''.format(adult, young))


