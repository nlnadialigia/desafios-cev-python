def fatorial(n, show=False):
    """
    => Cálculo do fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    print('*' * 30)
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


# Programa principal
print(fatorial(5, show=True))
print(fatorial(5))
