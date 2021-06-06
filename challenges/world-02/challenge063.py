color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
num = int(input('Digite um número: '))
c = 0
n = []
while c < (num - 1):
    if c == 0:
        n.append(0)
    elif c == 1:
        n.append(1)
    else:
        a = n[c - 1] + n[c - 2]
        n.append(a)
    c += 1
print('\33[1;35m {}'.format(n))
print('FIM')

print(color)
print('Resolução do Professor: ', end='')
print(clear)
print('\33[1;33m')
print('-' * 40)
print('Sequencia de Fibonacci'.center(40))
print('-' * 40)
print('\33[m', end='')
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('\33[1;32m~' * 40)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
   t3 = t1 + t2
   print(' -> {}'.format(t3), end='')
   t1 = t2
   t2 = t3
   cont += 1
print(' -> FIM')
print('~' * 40)
