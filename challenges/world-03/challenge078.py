color = '\33[1;35m'
clear = '\33[0;0m'
lista = list()

print(color)
print('Minha Resolução: ', end='')
print(clear)
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-' * 40)
print(f'Você digitou os valores {lista}')

maior = max(lista)
menor = min(lista)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, n in enumerate(lista):
    if n == maior:
        print(f'{p}...', end=' ')
print('')

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for p, n in enumerate(lista):
    if n == menor:
        print(f'{p}...', end='')
print('')
