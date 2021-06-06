numbers = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
user = int(input('Digite um número entre 0 e 20: '))
while user < 0 or user > 20:
    print('Tente novamente.', end=' ')
    user = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numbers[user]}')

print(color)
print('Resolução do Professor: ', end='')
print(clear)

while True:
    user = int(input('Digite um número entre 0 e 20: '))
    if 0 <= user <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {numbers[user]}')
