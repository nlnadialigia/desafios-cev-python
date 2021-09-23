color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
num = int(input('Escolha um número para a tabuada: '))
print('*' * 15)
print('\33[1;33m TABUADA DO {} \33[m'.format(num))
print('*' * 15)
for c in range(1, 11):
    print('{:3} x {:2} = {:2}'.format(num, c, (c * num)))
print('*' * 15)
