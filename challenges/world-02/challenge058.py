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

print(color)
print('Resolução do Professor: ', end='')
print(clear)
print('-=-'*25)
print('Sou seu computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1)
print('Será que você consegue adivinhar qual foi?')
sleep(1)
print('-=-'*25)
sleep(3)
palpites = 0
acertou = False
while not acertou:
    player = int(input('Qual é seu palpite? '))
    palpites += 1
    if player == computer:
        acertou = True
    else:
        if player < computer:
            print('\33[1;31mMais...\33[m', end=' ')
        else:
            print('\33[1;34mMenos...\33[m', end=' ')
        print('Tente mais uma vez.')
print('Você acertou com {} tentativas! Parabéns!'.format(palpites))
