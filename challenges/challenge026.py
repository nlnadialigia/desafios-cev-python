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

print(color)
print('Resolução do Professor: ', end='')
print(clear)
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
