def aumentar(n, p, m=True):
    """
    => Função que retorna o valor depois de sofrer acréscimo
    :param n: valor
    :param p: percentagem de acréscimo
    :param m: valor booleano que diz se a função será ou não formatada pela função moeda()
    :return: valor reajustado
    """
    valor = n + (n * p / 100)
    if m:
        return moeda(valor)
    else:
        return valor


def diminuir(n, p, m=True):
    """
    => Função que retorna o valor depois de sofrer desconto
    :param n: valor
    :param p: percentagem de desconto
    :param m: valor booleano que diz se a função será ou não formatada pela função moeda()
    :return: valor após desconto
    """
    valor = n - (n * p / 100)
    if m:
        return moeda(valor)
    else:
        return valor


def dobro(n, m=True):
    """
    => Função que retorna o dobro do valor
    :param n: valor
    :param m: valor booleano que diz se a função será ou não formatada pela função moeda()
    :return: o dobro do valor
    """
    valor = n * 2
    if m:
        return moeda(valor)
    else:
        return valor


def metade(n, m=True):
    """
    => Função que retorna a metade do valor
    :param n: valor
    :param m: valor booleano que diz se a função será ou não formatada pela função moeda()
    :return: metade do valor
    """
    valor = n / 2
    if m:
        return moeda(valor)
    else:
        return valor


def moeda(n):
    """
    => Função que formata o valor em reais (R$)
    :param n: valor
    :return: valor formatado
    """
    valor = '{:.2f}'.format(n).replace('.', ',')
    return f'R${valor}'


def resumo(p, a, d):
    print('*' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('*' * 35)
    print(f'Preço analisado: '.ljust(20), end='')
    print(f'{moeda(p)}')
    print(f'Dobro do preço: '.ljust(20), end='')
    print(f'{dobro(p)}')
    print(f'Metade do preço: '.ljust(20), end='')
    print(f'{metade(p)}')
    print(f'{a}% de aumento: '.ljust(20), end='')
    print(f'{aumentar(p, a)}')
    print(f'{d}% de redução: '.ljust(20), end='')
    print(f'{aumentar(p, d)}')
    print('*' * 35)


