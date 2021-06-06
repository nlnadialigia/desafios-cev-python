color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
list = (n1, n2, n3, n4)
nine = 0
for c in list:
    if c == 9:
        nine += 1
print(f'O valor 9 apareceu {nine} vezes.')
if 3 in list:
    print(f'O valor 3 apareceu na {(list.index(3) + 1)}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('O valores pares digitados foram ', end='')
for c in list:
    if c % 2 == 0:
        print(f'{c} ', end='')

print(color)
print('Resolução do Professor: ', end='')
print(clear)
print(f'Você digitou os valores {list}')
list = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')),)
print(f'Você digitou os valores {list}')
print(f'O valor 9 apareceu {list.count(9)} vezes.')
if 3 in list:
    print(f'O valor 3 apareceu na {(list.index(3) + 1)}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('O valores pares digitados foram ', end='')
for c in list:
    if c % 2 == 0:
        print(f'{c} ', end='')
print('')
