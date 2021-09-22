color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

if a > b:
    print('\33[33mO primeiro valor é maior')
elif b > a:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
