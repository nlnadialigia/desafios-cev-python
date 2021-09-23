color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    c = 1
    while c <= 10:
        print(f'{c} x {num} = {(c * num):>2}'.center(40))
        c += 1
    print('\33[1;34m*\33[m' * 40)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
