color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
days = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados: '))
rentCar = (days * 60) + (km * 0.15)
print('O total a pagar é R${:.2f} por {} dias e {}km rodados.' .format(rentCar, days, km))
