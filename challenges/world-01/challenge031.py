color = '\33[1;35m'
clear = '\33[0;0m'
n = float(input('Qual a distância da sua viagem? '))

print(color)
print('Minha Resolução: ', end='')
print(clear)
if n < 200:
    print('O preço da passagem é R${:.2f}'.format(n * 0.5))
else:
    print('O preço da sua passagem é R${:.2f}'.format(n * 0.45))

print(color)
print('Resolução do Professor: ', end='')
print(clear)
print('Você está prestes a começar uma viagem de {}km.'.format(n))
if n <= 200:
    price = n * 0.50
else:
    price = n * 0.45
print('O preço da sua passagem é R${:.2f}'.format(price))

preco = n * 0.50 if n <= 200 else n * 0.45
print('O preço da sua passagem é R${:.2f}'.format(preco))
