from datetime import date

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

year = int(input('Qual o ano de nascimento? '))
age = date.today().year - year

print('\33[33m*\33[34m' * 10)
if age < 9:
    print('MIRIM')
elif 9 <= age < 14:
    print('INFANTIL')
elif 14 <= age < 19:
    print('JÚNIOR')
elif 19 <= age < 25:
    print('SÊNIOR')
else:
    print('MASTER')
print('\33[33m*\33[m' * 10)

