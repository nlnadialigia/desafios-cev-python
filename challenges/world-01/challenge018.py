from math import cos, sin, tan, pi, radians
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
rad = int(input('Digite um ângulo: '))
x = rad * pi / 180
print('O seno do ângulo {}° é {:.2f}.' .format(rad, sin(x)))
print('O coseno do ângulo {}° é {:.2f}' .format(rad, cos(x)))
print('A tangente do ângulo {}° é {:.2f}' .format(rad, tan(x)))
