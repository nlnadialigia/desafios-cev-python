from math import trunc
color = '\33[1;35m'
clear = '\33[0;0m'
n = float(input('Digite um número real: '))

print(color)
print('Minha Resolução: ', end='')
print(clear)
real = trunc(n)
print('O número inteiro referente ao número {} é {}' .format(n, real))
