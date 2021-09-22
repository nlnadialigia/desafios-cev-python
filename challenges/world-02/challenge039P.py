from datetime import date

color = '\33[1;35m'
clear = '\33[0;0m'
print(color)
print('Resolução do Professor: ', end='')
print(clear)
born = int(input('Ano do nascimento: '))
year = date.today().year
age = year - born
print('\33[1;36mQuem nasceu em {} tem {} anos em {}.\33[m'.format(born, age, year))

print('\33[30m*\33[m' * 70)

if age < 18:
    balance = 18 - age
    print('\33[1;34mAinda faltam {} anos para o alistamento'.format(18 - age))
    time = year + balance
    print('\33[1;34mSeu alistamento será em {}'.format(time))
elif age > 18:
    balance = age - 18
    print('\33[1;31mVocê já deveria ter se alsitado a {} anos\33[m'.format(age - 18))
    time = year - balance
    print('\33[1;31mSeu alistamento foi em {}'.format(time))
else:
    print('\33[7;30;43mVocê tem que se alistar IMEDIATAMENTE!')
print('\33[30m*\33[m' * 70)


