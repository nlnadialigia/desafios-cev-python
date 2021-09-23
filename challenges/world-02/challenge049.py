color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
num = int(input('Escolha um número para a tabuada: '))
print('*' * 15)
print(' TABUADA DO {} '.format(num))
print('*' * 15)
for c in range(1, 11):
    print('{:3} x {:2} = {:2}'.format(c, num, (c * num)))
print('*' * 15)
