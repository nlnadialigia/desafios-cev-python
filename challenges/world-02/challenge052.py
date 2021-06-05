color = '\33[1;35m'
clear = '\33[0;0m'
n = int(input('Digite um número: '))

print(color)
print('Resolução do Professor: ', end='')
print(clear)
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
if tot == 2:
    print('\33[m')
    print('\nO número {} é PRIMO!'.format(n))
else:
    print('\nO número {} NÃO É PRIMO!'.format(n))
