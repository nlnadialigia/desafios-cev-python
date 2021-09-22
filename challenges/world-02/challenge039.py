from datetime import date

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
year = int(input('Qual o ano do seu nascimento? '))
age = date.today().year - year

print('\33[30m*\33[m' * 70)

if age < 18:
    print('\33[1;34mVocê é muito novo para se alistar! Volte daqui a {} anos'.format(18 - age))
elif age > 18:
    print('\33[1;31mVocê está atrasado! Deveria ter se alsitado a {} anos atrás\33[m'.format(age - 18))
else:
    print('\33[7;30;43mVem vindo ao alistamento militar!')
print('\33[30m*\33[m' * 70)
