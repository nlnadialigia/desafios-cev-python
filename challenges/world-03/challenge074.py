from random import randint

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
numbers = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
maior = menor = 0
print(f'Os valores sorteados foram: {numbers}')
for c in numbers:
    if c == 0:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
