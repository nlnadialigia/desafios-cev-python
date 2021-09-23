from random import randint
from time import sleep

color = '\33[1;35m'
clear = '\33[0;0m'
computer = randint(0, 10)

print(color)
print('Minha Resolução: ', end='')
print(clear)
print('-=-'*25)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*25)
player = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
count = 0
while player != computer:
    player = int(input('Você errou. Tente novamente! => '))
    count += 1
print('Você acertou depois de {} tentativas!'.format(count))

