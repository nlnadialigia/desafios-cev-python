from random import randint
from time import sleep

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

game = list()

print('*' * 50)
print('JOGO NA MEGA SENA'.center(50))
print('*' * 50)
qtde_games = int(input('Quantos jogos você quer que eu sorteie? '))
sleep(1)
print(f'SORTEANDO {qtde_games} JOGOS'.center(50, '*'))
sleep(1)
for n in range(0, qtde_games):
    for i in range(0, 6):
        game.append(randint(1, 61))
    print(f'Jogo {n+1}: {game}')
    game = list()
    sleep(1)

