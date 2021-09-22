from random import randint

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
from random import randint
numbers = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for c in numbers:
    print(f'{c} ', end='')
print('')
print(f'O maior valor sorteado foi {max(numbers)}')
print(f'O menor valor sorteado foi {min(numbers)}')
