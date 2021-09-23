from math import pow

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
peso = float(input('Qual seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / pow(1.80, 2)
print('IMC: {}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc <= 40:
    print('Obesidade')
else:
    print('Obsidade Mórbida')


