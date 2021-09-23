color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
greater = 0
smaller = 1000
for c in range(0, 5):
    weight = float(input('Peso (kg): '))
    if weight > greater:
        greater = weight
    elif weight < smaller:
        smaller = weight
print('''
    Maior peso: {}
    Menor peso: {}'''.format(greater, smaller))

