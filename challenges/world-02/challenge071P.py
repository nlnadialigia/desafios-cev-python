color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
print('\33[1;31m', end='')
print('=' * 40)
print('BANCO CEV'.center(40))
print('=' * 40, '\33[m', end='')
print('\33[m')
value = int(input('Que valor você quer sacar? R$'))
total = value
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('\33[1;31m', end='')
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
