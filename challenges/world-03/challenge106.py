# FUNDOS
verde = '\033[0;42m'
azul = '\033[0;44m'
vermelho = '\033[0;41m'
brancoF = '\033[0;107m'

# LETRAS
preto = '\033[30m'
brancoL = '\033[97m'

reset = '\033[0;0m'


def cabecalho(titulo, fundo, letra):
    """
    => Retorna o cabeçalho formatado
    :param titulo: nome do cabeçalho
    :param fundo: cor de fundo
    :param letra: cor da letra
    :return: retorno vazio
    """
    print(fundo, letra, end='')
    print('~' * (len(titulo) + 5))
    print('', titulo.center(len(titulo) + 5))
    print('', '~' * (len(titulo) + 5), end='')
    return ''


def ajuda(nome):
    """
    => Retorna o manual do respectivo comando
    :param nome: comando a ser buscado
    :return: none
    """
    cabecalho(f'Acessando o manual do comando {nome}', azul, brancoL)
    print()
    print(brancoF, preto, end='')
    help(nome)


while True:
    print(cabecalho('SISTEMA DE AJUDA PyHELP', verde, preto))
    print(reset)
    lib = str(input('Função ou Biblioteca > ')).lower()
    if lib == 'fim':
        print(cabecalho('ATÉ LOGO!', vermelho, brancoL))
        break
    else:
        ajuda(lib)
