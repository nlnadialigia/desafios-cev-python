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
