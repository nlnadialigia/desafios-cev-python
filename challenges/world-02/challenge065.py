color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

choice = 'S'
list = []
sum = 0
avarage = 0
maior = 0
menor = 0
while choice == 'S':
    num = int(input('Digite um número: '))
    list.append(num)
    sum += num
    avarage = sum / len(list)
    if len(list) == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    choice = str(input('Quer digitar um novo valor? [S/N]: ')).upper()
print('A soma dos números digitados é {}'.format(sum))
print('A média entre todos os valores é {}'.format(avarage))
print('O maior número digitado é {}'.format(maior))
print('O menr número digitado é {}'.format(menor))

print(color)
print('Resolução do Professor: ', end='')
print(clear)
choice = 'S'
list = []
sum = qtde = avarage = maior = menor = 0
while choice in 'Ss':
    num = int(input('Digite um número: '))
    sum += num
    qtde += 1
    if qtde == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    choice = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
avarage = sum / qtde
print('Você digitou {} números e a média foi {:.2f}'.format(qtde, avarage))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))
