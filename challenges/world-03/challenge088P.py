from random import randint
from time import sleep

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução Professor: ', end='')
print(clear)

print('*' * 50)
print('JOGO NA MEGA SENA'.center(50))
print('*' * 50)
qtde_games = int(input('Quantos jogos você quer que eu sorteie? '))
sleep(1)
print(f'SORTEANDO {qtde_games} JOGOS'.center(50, '*'))
sleep(1)

lista = list()
games = list()
tot = 0

while tot < qtde_games:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    games.append(lista[:])
    lista.clear()
    tot += 1

for i, l in enumerate(games):
    print(f'Jogo {i+1}: {l}')
