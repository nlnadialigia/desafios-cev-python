color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
num = int(input('Digite um número: '))
fat = 1
print('{}! é igual a '.format(num), end='')
while num >= 1:
    fat = fat * num
    num -= 1
print(fat)

for c in range(num, 0, -1):
    fat = fat * num
print(fat)


