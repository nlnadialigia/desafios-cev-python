color = '\33[1;35m'
clear = '\33[0;0m'
lista = list()

n = ' '
print(color)
print('Resolução do Professor: ', end='')
print(clear)
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    choice = str(input('Quer continuar? [S/N] '))
    if choice in 'Nn':
        break
print('-=' * 40)
lista.sort()
print(f'Você digitou os valores {lista}')
