color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
phrase = str(input('Frase: ')).upper().strip().replace(' ', '')
d = len(phrase)-1
x = True
for c in range(0, len(phrase)):
    if phrase[c] != phrase[d]:
        x = False
        print('A FRASE NÃO É PALÍNDROMO!')
        break
    d = d-1
if x:
    print(' A FRASE É UM PALÍNDROMO!')
print('FIM')