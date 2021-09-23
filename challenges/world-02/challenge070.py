color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

print('\33[1;34m', end='')
print('-' * 40)
print('LOJA SUPER BARATÃO'.center(40))
print('-' * 40, end='')
print('\33[m')
choice = name = product = ''
total = expensive = price = cheap = 0
while True:
    product = str(input('Nome do Produto: ')).strip().title()
    price = float(input('Preço: R$'))
    choice = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    total += price
    if price > 1000:
        expensive += 1
    if choice in 'Nn':
        break
print('\33[1;34m', end='')
print('FIM DO PROGRAMA'.center(40, '-'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {expensive} produtos custando mais de R$1000.00')


