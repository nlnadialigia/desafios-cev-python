from random import choice
from random import randint
from time import sleep
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
list = [0, 1, 2, 3, 4, 5]
n = choice(list)
num = int(input('Advinhe o número!\n Digite um número de 0 a 5: '))

if num > 5:
    print('Desculpa, mas o número tem que ser de 0 a 5')
else:
    if num == n:
        print('Parabéns, você acertou!')
    else:
        print('Você errou! O número era {}'.format(n))


