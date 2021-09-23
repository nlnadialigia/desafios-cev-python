color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
# MATH
f = factorial(num)
print('\33[1;34m')
print('=*' * 25)
print('O fatorial de {} é {}'.format(num, f))
print('=*' * 25)
print('\33[m')

fat = 1
c = num
print('\33[31m')
print('=*' * 25)
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
print('{}'.format(fat))
print('=*' * 25)
print('\33[m')

