a = [2, 3, 4, 7]
b = a

print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('')

b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('')

c = a[:] #cria uma cópia de a
print(f'Lista A: {a}')
print(f'Lista C: {c}')
print('')

c[2] = 15
print(f'Lista A: {a}')
print(f'Lista C: {c}')
print('')
