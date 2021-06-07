lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])

print('\33[1;33m')
print(' FOR / IN '.center(30, '*'))
print('\33[m')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('*' * 30)

print('\n\33[1;33m')
print(' FOR / RANGE '.center(30, '*'))
print('\33[m')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('*' * 30)

print('\n\33[1;33m')
print(' FOR / ENUMERATE '.center(30, '*'))
print('\33[m')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')

print(sorted(lanche))


