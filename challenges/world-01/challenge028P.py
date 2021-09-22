from random import choice
from random import randint
from time import sleep
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
computer = randint(0, 5)
print('-=-'*25)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*25)
player = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if player == computer:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computer, player))

