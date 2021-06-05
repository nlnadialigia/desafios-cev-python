from time import sleep
from random import randint
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)

itens = ('Pedra', 'Papel', 'Tesoura')
computer = randint(0, 2)

print('\33[1;31mVamos jogar Jokenpô?\33[m')
print('''Suas opções:
\33[1;94m 0 => PEDRA
\33[1;92m 1 => PAPEL
\33[1;91m 2 => TESOURA
\33[m''')
player = int(input('Qual é sua jogada: '))
print(computer)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 20)
print('Computador jogou {}'.format(itens[computer]))
print('Jogador jogou {}'.format(itens[player]))
print('-=' * 20)

if computer == player:
    print('EMPATE')
else:
    if computer == 0:
        if player == 1:
            print('JOGADOR VENCE')
            print('Papel embrulha a pedra!')
        elif player == 2:
            print('COMPUTADOR VENCE')
            print('Pedra quebra tesoura!')
        else:
            print('JOGADA INVÁLIDA!')

    elif computer == 1:
        if player == 0:
            print('COMPUTADOR VENCE')
            print('Papel embrulha a pedra!')
        elif player == 2:
            print('JOGADOR VENCE')
            print('Tesoura corta o papel')
        else:
            print('JOGADA INVÁLIDA!')

    elif computer == 2:
        if player == 0:
            print('JOGADOR VENCE')
            print('Pedra quebra tesoura!')
        elif player == 1:
            print('COMPUTADOR VENCE')
            print('Tesoura corta o papel')
        else:
            print('JOGADA INVÁLIDA!')
