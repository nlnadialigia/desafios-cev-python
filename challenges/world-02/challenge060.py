color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
num = int(input('Digite um número: '))
fat = 1
print('{}! é igual a '.format(num), end='')
while num >= 1:
    fat = fat * num
    num -= 1
print(fat)

for c in range(num, 0, -1):
    fat = fat * num
print(fat)

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

