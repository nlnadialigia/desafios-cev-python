from math import trunc
color = '\33[1;35m'
clear = '\33[0;0m'
n = float(input('Digite um número real: '))

print(color)
print('Resolução do Professor: ', end='')
print(clear)
print('O valor digitado foi {} e a sua porção inteira é {}' .format(n, trunc(n)))

print(color)
print('Resolução 2 do Professor: ', end='')
print(clear)
print('O valor digitado foi {} e a sua porção inteira é {}' .format(n, int(n)))

