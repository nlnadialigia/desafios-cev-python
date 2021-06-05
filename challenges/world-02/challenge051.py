color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução: ', end='')
print(clear)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('\33[1;95m*\33[m' * 30)
print('PROGRESSÃO ARITMÉTICA')
print('\33[1;95m*\33[m' * 30)
for c in range(1, 11):
    n = t + ((c - 1) * r)
    print(n, end=' ')

