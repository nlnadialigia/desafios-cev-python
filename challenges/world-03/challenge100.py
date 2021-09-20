from random import randint
from time import sleep

numeros = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        numeros.append(randint(0, 100))
    for n in numeros:
        print(f'{n} ', end='')
        sleep(0.5)
    print('PRONTO!')


def soma_par():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()
soma_par()
