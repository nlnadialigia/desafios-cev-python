color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

numbers = list()
even = list()
odd = list()
numbers.append(even)
numbers.append(odd)
for i in range(0, 7):
    n = int(input(f'Digite {i+1}º valor: '))
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print('-=' * 50)
print(f'Os valores pares digitados foram: {sorted(even)}')
print(f'Os valores ímpares digitados foram: {sorted(odd)}')
print(numbers)
