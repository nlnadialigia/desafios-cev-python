color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

numbers = list()
even = list()
odd = list()
for i in range(0, 7):
    n = int(input(f'Digite {i+1}º valor: '))
    numbers.append(n)
    print(f'n: {n}, i: {i+1}, numbers: {numbers}')
    if n % 2 == 0:
        even.append(n)
        print(f'pares: {even}')
    else:
        odd.append(n)
        print(f'ímpares: {odd}')

print('-=' * 50)
print(f'Os valores pares digitados foram: {even}')
print(f'Os valores ímpares digitados foram: {odd}')
