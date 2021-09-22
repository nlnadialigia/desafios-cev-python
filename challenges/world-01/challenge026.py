color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
frase = str(input('Frase: '))
n = frase.count('a')
i = frase.rfind('a')
print('Quantas vezes aparece a letra A: {}'.format(n))
print('Posição que a letra A aparece a primeira vez: {}'.format(frase.find('a')))
print('Posição que a letra A aparece pela última vez: {}'.format(frase.rfind('a')))

