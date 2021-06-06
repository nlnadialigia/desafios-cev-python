color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
choice = 0
while choice != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print('''O que você deseja fazer?
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    choice = int(input('Opção desejada? '))
    if choice == 1:
        print('A soma de {} e {} é {}'.format(n1, n2, n1 + n2))
        choice = 5
    if choice == 2:
        print('A multiplicação de {} e {} é igual a {}.'.format(n1, n2, n1 * n2))
        choice = 5
    if choice == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
            choice = 5
        else:
            print('{} é maior que {}.'.format(n2, n1))
            choice = 5
print('FIM')

print(color)
print('Resolução do Professor: ', end='')
print(clear)
from time import sleep
choice = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while choice != 5:
    print('''\33[1;34m
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    \33[m''', end='')
    choice = int(input('>>>>>Opção desejada? '))
    print('\33[1;35m')
    if choice == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    elif choice == 2:
        print('O resultado de {} x {} é igual a {}.'.format(n1, n2, n1 * n2))
    elif choice == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        else:
            print('{} é maior que {}.'.format(n2, n1))
    elif choice == 4:
        print('\33[mInforme os números novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif choice == 5:
        print('FINALIZANDO...')
    else:
        print('\33[1;31mOpção inválida. Tente novamente.\33[m')
    sleep(2)
print('\33[30;45mFim do programa! Volte sempre!\33[m')

