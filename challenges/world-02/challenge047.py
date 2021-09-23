color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
for c in range(1, 50):
    if c % 2 == 0:
        print(c, end=' ')
print('\nFIM')

