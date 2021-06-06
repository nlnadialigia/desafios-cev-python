lista = list()
pair = list()
odd = list()

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
while True:
    choice = ' '
    lista.append(int(input('Digite um número: ')))
    while choice not in 'SN':
        choice = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if choice == 'N':
        break
print('-=' * 40)
print(f'A lista completa é {lista}')
for n in lista:
    if n % 2 == 0:
        pair.append(n)
    else:
        odd.append(n)
print(f'A lista de pares é {pair}')
print(f'A lista de ímpares é {odd}')

print(color)
print('Resolução do Professor: ', end='')
print(clear)
while True:
    lista.append(int(input('Digite um número: ')))
    choice = str(input('Quer continuar? [S/N] '))
    if choice in 'Nn':
        break
print('-=' * 40)
print(f'A lista completa é {lista}')
for n in lista:
    if n % 2 == 0:
        pair.append(n)
    else:
        odd.append(n)
print(f'A lista de pares é {pair}')
print(f'A lista de ímpares é {odd}')
