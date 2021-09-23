from random import randint
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
print('\33[1;34m*' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(30))
print('\33[1;34m*\33[m' * 30)
v = 0
while True:
    player = int(input('Diga um valor: '))
    computer = randint(0, 10)
    total = player + computer
    type = ' '
    while type not in 'PI':
        type = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {player} e o cumputador {computer}. Total de {total}, ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if type == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif type == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes!')
