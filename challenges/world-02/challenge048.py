color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
