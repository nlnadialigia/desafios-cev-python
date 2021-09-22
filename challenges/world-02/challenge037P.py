from pyconverter import inttobin, inttohex, bintooct

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)

num = int(input('Digite um número: '))
print('\33[1;96m*\33[m' * 50)
print('''Qual a base de conversão?
[ 1 ] - BINÁRIO
[ 2 ] - OCTAL
[ 3 ] - HEXADECIMAL''')
base = int(input('Sua opção: '))
print('\33[1;96m*\33[m' * 50)

if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA! Tente novamente.')
