def aumentar(n, p, m):
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


def diminuir(n, p, m):
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


def dobro(n, m):
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


def metade(n, m):
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
