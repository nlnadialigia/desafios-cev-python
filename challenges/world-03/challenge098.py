from time import sleep


def contador(i, f, p):
    # Passo negativo
    if p < 0:
        p *= (-1)
    # Passo igual a 0
    if p == 0:
        p = 1

    print(f'Contagem de {i} até {f} de {p} em {p}')
    # inicio < fim
    if i <= f:
        while i <= f:
            print(f'{i} ', end="")
            i += p
            sleep(0.5)
        print('FIM!')
    else:
        # inicio > fim
        while i >= f:
            print(f'{i} ', end='')
            i -= p
            sleep(0.5)
        print('FIM!')
    print('-=' * 50)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)


