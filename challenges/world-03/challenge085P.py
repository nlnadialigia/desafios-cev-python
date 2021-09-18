color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução Professor: ', end='')
print(clear)

num = [[], []]

for i in range(0, 7):
    n = int(input(f'Digite {i+1}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(num)

num[0].sort()
num[1].sort()

print('-=' * 50)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
