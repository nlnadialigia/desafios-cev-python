color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

matriz = [[0 for i in range(3)] for j in range(3)]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 40)
for linha in range(3):
    for coluna in range(3):
        print("%4d" % matriz[linha][coluna], end='')
    print()
print('-=' * 40)

