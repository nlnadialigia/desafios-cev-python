color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
product = float(input('Preço do produto: R$'))

print('\33[31mEscolha a condição de pagamento:\33[m')
choice = int(input('''\33[34mDigite: 
    - 1 => à vista em dinheiro/cheque
    - 2 => à vista no cartão
    - 3 => em até 2x no cartão
    - 4 => 3x ou mais no cartão
'''))

print('\33[35m*\33[m' * 80)
print('\33[34m')
price = product
if choice == 1:
    price = product - (product * 0.10)
elif choice == 2:
    price = product - (product * 0.05)
elif choice == 3:
    price = product
elif choice == 4:
    price = product + (product * 0.20)
else:
    print('\33[1;31mOpção inválida!\33[m')

if 1 <= choice <= 4:
    print('O valor do produto será R${:.2f}'.format(price))
else:
    print('\33[1;31mPor favor, digite uma opção válida!\33[m')

print('\33[m')
print('\33[35m*\33[m' * 80)
