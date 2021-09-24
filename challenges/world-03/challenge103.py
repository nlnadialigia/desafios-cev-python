def ficha(nome="<desconhecido>", qtde=0):
    """
    => Retorna a ficha do jogador
    :param nome: (opcional) nome do jogador
    :param qtde: (opcional) quantidade de gols feito
    :return: none
    """
    print(f'O jogador {nome} fez {qtde} gol(s) no campeonato.')


print('*' * 30)
nome = str(input('Nome do Jogador: ')).strip()
qtde = str(input('Número de Gols: '))
ficha()
