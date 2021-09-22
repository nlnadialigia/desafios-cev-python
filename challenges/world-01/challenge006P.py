color = '\33[1;35m'
clear = '\33[0;0m'
n = int(input('Digite um número: '))

print(color)
print('Resolução 1 do Professor: ', end='')
print(clear)
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro {} vale {}' .format(n, d))
print('O triplo {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}' .format(n, t, n, r))

print(color)
print('Resolução 2 do Professor: ', end='')
print(clear)
raizQuadrada = pow(n, 1/2)
print('A raiz quadrada de {} é {:.2f}' .format(n, raizQuadrada))

