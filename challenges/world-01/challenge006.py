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
