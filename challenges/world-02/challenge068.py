from random import randint
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

computer = randint(0, 100)
print('\33[1;34m*' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(30))
print('\33[1;34m*\33[m' * 30)
qtde = 0
while True:
    player = int(input('Diga um valor: '))
    choice = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    total = player + computer
    response = choice
    if total % 2 == 0:
        response = 'PAR'
    else:
        response = 'IMPAR'
    print(f'Você jogou {player} e o cumputador {computer}. Total de {total} deu {response}')
    if response[0] != choice:
        print('GAME OVER.')
        print(f'Você venceu {qtde} vezes.')
        break
    else:
        qtde += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')

