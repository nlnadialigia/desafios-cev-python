color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

print('\33[1;31m', end='')
print('=' * 40)
print('BANCO CEV'.center(40))
print('=' * 40, '\33[m', end='')
print('\33[m')
value = float(input('Que valor você quer sacar? R$'))
integer = value
fifty = twenty = ten = unity = int(0)

if integer // 50 != 0:
    fifty = value // 50
    integer = value - (fifty * 50)
    print(f'Total de {int(fifty)} cédulas de R$50')
if integer // 20 != 0:
    twenty = integer // 20
    integer = integer - (twenty * 20)
    print(f'Total de {int(twenty)} cédulas de R$20')
if integer // 10 != 0:
    ten = integer // 10
    integer = integer - (ten * 10)
    print(f'Total de {int(ten)} cédulas de R$10')
if integer != 0:
    unity = integer
    integer = integer - unity
    print(f'Total de {int(unity)} cédulas de R$1')
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
