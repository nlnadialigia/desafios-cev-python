color = '\33[1;35m'
clear = '\33[0;0m'
lista = list()

print(color)
print('Resolução do Professor: ', end='')
print(clear)
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('=-' * 40)
print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, n in enumerate(lista):
    if n == maior:
        print(f'{p}...', end=' ')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for p, n in enumerate(lista):
    if n == menor:
        print(f'{p}...', end='')
print()