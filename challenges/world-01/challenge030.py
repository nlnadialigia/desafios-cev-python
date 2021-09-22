color = '\33[1;35m'
clear = '\33[0;0m'
num = int(input('Digite um número inteiro: '))

print(color)
print('Minha Resolução: ', end='')
print(clear)
if num % 2 == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))

