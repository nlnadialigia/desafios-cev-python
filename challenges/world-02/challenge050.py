color = '\33[1;35m'
clear = '\33[0;0m'
s = 0
print('Digite 6 números inteiros:')

print(color)
print('Minha Resolução: ', end='')
print(clear)
for c in range(0, 6):
    n = int(input('number: '))
    if n % 2 == 0:
        s += n
print('A soma dos números pares digitados é {}'.format(s))

