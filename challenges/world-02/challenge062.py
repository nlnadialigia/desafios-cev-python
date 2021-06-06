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

choice = ''
print('''\nSe desejar mostrar mais termos digite a quantidade de termos, senão digite [ 0 ]''')
while choice != 0:
    choice = int(input('Opção: '))
    d = c + choice
    while c < d:
        n = t + ((c - 1) * r)
        c += 1
        print(n, end=' -> ')
print('\nFIM')

print(color)
print('Resolução do Professor: ', end='')
print(clear)
print('\33[1;95m*\33[m' * 70)
print('PROGRESSÃO ARITMÉTICA'.center(70))
print('\33[1;95m*\33[m' * 70)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
choice = ''
total = 0
choice = 10
while choice != 0:
    total += choice
    while c <= total:
        print('{}'.format(t), end=' -> ')
        t += r
        c += 1
    print('PAUSA')
    choice = int(input('Quantos termos você quer mostrar a mais: '))

print('\nA progressão foi finalizada com {} termos mostrados.'.format(total))


