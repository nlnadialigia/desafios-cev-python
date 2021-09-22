from math import hypot, trunc
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
a = int(input('Qual o comprimento do cateto oposto? '))
b = int(input('Qual o comprimento do cateto adjacente? '))
h = hypot(a, b)
print('A hitpotenusa do triângulo é {}' .format(trunc(h)))
