color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
from datetime import date
year = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é bissexto'.format(year))
else:
    print('O ano {} não é bissexto'.format(year))

