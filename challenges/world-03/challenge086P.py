color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução Professor: ', end='')
print(clear)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print(matriz)

print('-=' * 40)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=' * 40)

