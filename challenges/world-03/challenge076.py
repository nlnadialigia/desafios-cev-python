color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução: ', end='')
print(clear)

products = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-' * 40)
for c in range(len(products)):
    if c % 2 == 0:
        print(f'{products[c]:.<30}', end='')
    else:
        print('R$', end='')
        print(f'{products[c]:.2f}'.rjust(7))
print('-' * 40)
