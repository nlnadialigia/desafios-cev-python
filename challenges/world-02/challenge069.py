color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

print('\33[1;94m', end='')
print('-' * 40)
print('CADASTRE UMA PESSOA'.center(40))
print('-' * 40)
print('\33[m', end='')
a = b = c = 0
while True:
    age = int(input('Idade: '))
    gender = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while gender not in 'MmFf':
        gender = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 40)
    choice = str(input('Quer continuar? [S/N] '))
    while choice not in 'SsNn':
        choice = str(input('Quer continuar? [S/N] '))
    print('-' * 40)
    if age >= 18:
        a += 1
    if gender in 'Mm':
        b += 1
    if gender in 'Ff':
        if age < 20:
            c += 1
    if choice in 'Nn':
        break
print(' FIM DO PROGRAMA '.center(40, '='))
print(f'Total de pessoas com mais de 18 anos: {a}')
print(f'Ao todo temos {b} homens cadastrados.')
print(f'E temos {c} mulheres com menos de 20 anos.')
