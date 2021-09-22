color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)

lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    choice = str(input('Quer continuar? [S/N] '))
    if choice in 'Nn':
        break
print('-=' * 40)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')