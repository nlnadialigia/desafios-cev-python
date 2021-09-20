from time import sleep


def contador():
    print('-=' * 50)
    print('Contagem de 1 até 10 de 1 em 1')
    n = 1
    while n <= 10:
        print(f'{n} ', end='')
        sleep(0.5)
        n += 1
    print('FIM!')
    print('-=' * 50)
    print('Contagem de 10 até 0 de 2 em 2')
    x = 10
    while x >= 0:
        print(f'{x} ', end='')
        x -= 2
        sleep(0.5)
    print('FIM')
    print('-=' * 50)
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    print('-=' * 50)

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


contador()

