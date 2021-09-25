def notas(*n, sit=False):
    """
    => Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """

    media = sum(n) / len(n)
    rel = dict()
    rel['total'] = len(n)
    rel['maior'] = max(n)
    rel['menor'] = min(n)
    rel['media'] = media
    if sit:
        if media >= 7:
            rel['situação'] = 'BOA!'
        elif media >= 5:
            rel['situação'] = 'RAZOÁVEL!'
        else:
            rel['situação'] = 'RUIM!'
    return rel


# Programa principal
resp = notas(8, 0, sit=True)
print(resp)
