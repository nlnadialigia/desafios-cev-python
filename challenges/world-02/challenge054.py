from datetime import date
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
year = date.today().year
adult = 0
young = 0
for c in range(0, 7):
    birth = int(input('Ano do nascimento: '))
    age = year - birth
    if age < 21:
        young += 1
    else:
        adult += 1
print('''
    Atingiram a MAIORIDADE: {}
    NÃO atingiram a MAIORIDADE: {}'''.format(adult, young))

print(color)
print('Resolução do Professor: ', end='')
print(clear)
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))

