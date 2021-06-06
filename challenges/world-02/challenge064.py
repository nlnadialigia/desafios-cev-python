color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
num = 0
sum = 0
count = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        sum += num
        count += 1
print('Foram digitados {} números e a soma entre eles é {}'.format(count, sum))

print(color)
print('Resolução do Professor: ', end='')
print(clear)
num = sum = count = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    sum += num
    count += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Foram digitados {} números e a soma entre eles é {}'.format(count, sum))
