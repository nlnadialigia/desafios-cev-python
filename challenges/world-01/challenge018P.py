from math import cos, sin, tan, radians
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
angulo = int(input('Digite um ângulo: '))
x = radians(angulo)
print('O seno do ângulo {}° é {:.2f}' .format(angulo, sin(x)))
print('O coseno do ângulo {}° é {:.2f}' .format(angulo, cos(x)))
print('A tangente do ângulo {}° é {:.2f}' .format(angulo, tan(x)))
