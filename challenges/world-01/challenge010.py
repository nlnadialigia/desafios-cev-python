color = '\33[1;35m'
clear = '\33[0;0m'
n = float(input('Quanto dinheiro você tem na carteira? '))
exchange = 3.27

print(color)
print('Minha Resolução: ', end='')
print(clear)
result = n / exchange
print('Você tem R${:.2f}, que corresponde a US${:.2f}' .format(n, result))




