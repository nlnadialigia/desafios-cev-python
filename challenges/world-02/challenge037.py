from pyconverter import inttobin, inttohex, bintooct

color = '\33[1;35m'
clear = '\33[0;0m'
n = int(input('Digite um número: '))

print(color)
print('Minha Resolução: ', end='')
print(clear)

print('\33[1;96m*\33[m' * 30)
base = int(input('''Qual a base de conversão?
1 - binário
2 - octal
3 - hexadecimal
'''))
print('\33[1;96m*\33[m' * 30)
b = inttobin(n)
h = inttohex(n)
o = bintooct(b)

if base == 1:
    print(b)
elif base == 2:
    print(h)
else:
    print(o)

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
