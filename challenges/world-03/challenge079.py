color = '\33[1;35m'
clear = '\33[0;0m'
lista = list()

print(color)
print('Minha Resolução: ', end='')
print(clear)
n = ' '
while True:
    choice = ' '
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    while choice not in 'SN':
        choice = str(input('Quer continuar? [S/N] ')).upper()
    if choice == 'N':
        break
print('-=' * 40)
print(f'Você digitou os valores {lista}')
