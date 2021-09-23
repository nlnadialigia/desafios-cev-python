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

