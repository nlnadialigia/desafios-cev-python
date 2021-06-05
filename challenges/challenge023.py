color = '\33[1;35m'
clear = '\33[0;0m'
num = int(input('Digite um número de 0 a 9999: '))

print(color)
print('Minha Resolução: ', end='')
print(clear)

unidade = num % 10
numC = num // 10

dezena = numC % 10
numD = numC // 10

centena = numD % 10
milhar = numD // 10

print('=' * 50)
print('NUMBER')
print('unidade: ', unidade)
print('dezena: ', dezena)
print('centena: ', centena)
print('milhar: ', milhar)

string = '000' + str(num)
print('=' * 50)
print('STRING')
x = len(string)
print('unidade: {}' .format(string[x-1]))
print('dezena: {}' .format(string[x-2]))
print('centena: {}' .format(string[x-3]))
print('milhar: {}' .format(string[x-4]))

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
