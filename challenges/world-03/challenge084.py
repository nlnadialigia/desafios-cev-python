color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

people = list()
choice = ''

while choice in 'Ss':
    name = str(input('Nome: '))
    weight = float(input('Peso: '))
    people.append([name, weight])
    choice = str(input('Quer continuar? [S/N] '))

print('-=' * 40)

print(f'Ao todo você cadastrou {len(people)} pessoas.')

maior = menor = people[0][1]
print(f'Maior e menor = {maior}')
name_maior = name_menor = list()
for person in people:
    if person[1] > maior:
        maior = person[1]
    if person[1] < menor:
        menor = person[1]

print(f'menor: {menor}')
print(f'maior: {maior}')

for n in people:
    print(n)
    if n[1] == maior:
        name_maior = n[0]
    if n[1] == menor:
        name_menor = n[0]


print(f'O maior peso foi de {maior}kg. Peso de {name_maior}')
print(f'O menor peso foi de {menor}kg. Peso de {name_menor}')
