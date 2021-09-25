def ficha(nome="<desconhecido>", gol=0):
    """
    => Retorna a ficha do jogador
    :param nome: (opcional) nome do jogador
    :param qtde: (opcional) quantidade de gols feito
    :return: none
    """
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


# Programa Princiapl
print('*' * 30)
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
