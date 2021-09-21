from random import randint
from time import sleep

numeros = list()


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for count in range(0, 5):
        n = randint(0, 100)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('PRONTO!')


def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia(numeros)
soma_par(numeros)
