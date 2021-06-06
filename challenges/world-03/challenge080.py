color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
lista = []
for c in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-=' * 40)
print(f'Os valores digitados em ordem foram {lista}')
