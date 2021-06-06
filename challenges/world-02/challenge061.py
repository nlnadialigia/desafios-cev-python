color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('\33[1;95m*\33[m' * 70)
print('PROGRESSÃO ARITMÉTICA'.center(70))
print('\33[1;95m*\33[m' * 70)

c = 1
while c <= 10:
    n = t + ((c - 1) * r)
    c += 1
    print(n, end=' -> ')
print('FIM')

print(color)
print('Resolução do Professor: ', end='')
print(clear)
print('\33[1;95m*\33[m' * 70)
print('PROGRESSÃO ARITMÉTICA'.center(70))
print('\33[1;95m*\33[m' * 70)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))

c = 1
while c <= 10:
    print(t, end=' -> ')
    t += r
    c += 1
print('FIM')
