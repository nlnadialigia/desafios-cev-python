color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
price = float(input('Digite o valor do produto: '))
discount = 5
total = price - (price * (discount/100))
print('O produto custa R${:.2f}, mas está com {:.2f}% de desconto, ' .format(price, discount), end='')
print('totalizando R${:.2f}.' .format(total))

