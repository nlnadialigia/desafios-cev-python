color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
# print(matriz)
#
matriz = [[10, 15, 20], [21, 18, 13], [9, 8, 3]]
soma = 0
somaColuna = 0
maiorValor = matriz[0][0]

print('-=' * 40)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=' * 40)

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma = soma + matriz[linha][coluna]
print(f'A soma dos valores pares é {soma}.')

for linha in range(0, 3):
    somaColuna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somaColuna}')

for coluna in range(0, 3):
    if matriz[1][coluna] > maiorValor:
        maiorValor = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maiorValor}')
