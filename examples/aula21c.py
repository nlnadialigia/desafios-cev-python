def somar(a, b, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return:
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(2, 8)
