color = '\33[1;35m'
clear = '\33[0;0m'
n = int(input('Digite um número: '))

print(color)
print('Minha resolução: ', end='')
print(clear)
print('O número digitado do é {}' .format(n))
print('O dobro de {} é {}' .format(n, n*2))
print('o triplo de {} é {}' .format(n, n*3))
print('A raiz quadrada de {} é {}' .format(n, int(n**(1/2))))

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

