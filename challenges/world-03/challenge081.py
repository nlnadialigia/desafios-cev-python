color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

count = 0
lista = list()
while True:
    choice = ' '
    lista.append(int(input('Digite um valor: ')))
    count += 1
    while choice not in 'NS':
        choice = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if choice == 'N':
        break
print('-=' * 40)
print(f'Você digitou {count} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
