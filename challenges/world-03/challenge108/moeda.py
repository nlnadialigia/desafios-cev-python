def aumentar(n, p):
    """
    => Função que retorna o valor depois de sofrer acréscimo
    :param n: valor
    :param p: porcentagem de acréscimo
    :return: valor reajustado
    """
    return n + (n * p / 100)


def diminuir(n, p):
    """
    => Função que retorna o valor depois de sofrer desconto
    :param n: valor
    :param p: porcentagem de desconto
    :return: valor após desconto
    """
    pass
    return n - (n * p / 100)


def dobro(n):
    """
    => Função que retorna o dobro do valor
    :param n: valor
    :return: o dobro do valor
    """
    return n * 2


def metade(n):
    """
    => Função que retorna a metade do valor
    :param n: valor
    :return: metade do valor
    """
    return n / 2


def moeda(n):
    valor = '{:.2f}'.format(n).replace('.', ',')
    return f'R${valor}'
