color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
qtde = sum = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    sum += num
    qtde += 1
print(f'Foram digitados \33[1;31m{qtde}\33[m números e a soma entre eles é \33[1;31m{sum}\33[m.')

print(color)
print('Resolução do Professor: ', end='')
print(clear)
qtde = sum = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    sum += num
    qtde += 1
print(f'Foram digitados \33[1;31m{qtde}\33[m números e a soma entre eles é \33[1;31m{sum}\33[m.')
