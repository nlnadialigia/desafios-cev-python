color = '\33[1;35m'
clear = '\33[0;0m'
num = int(input('Digite um número de 0 a 9999: '))

print(color)
print('Resolução do Professor: ', end='')
print(clear)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
