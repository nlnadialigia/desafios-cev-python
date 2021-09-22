color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
ano = int(input('Digite o ano com 4 dígitos: '))
string = str(ano)
d = ano % 100
c = ano % 1000

if string.rfind('00'):
    if c % 400 == 0:
        print('O ano {} é bissexto'.format(ano))
if d % 4 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano não é bissexto')
