from math import hypot, trunc
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
hi = hypot(co, ca)
hip = (co**2 + ca**2)**(1/2)
print('A hitpotenusa do triângulo é {:.2f}' .format(hi))
print('A hitpotenusa do triângulo é {:.2f}' .format(hip))
