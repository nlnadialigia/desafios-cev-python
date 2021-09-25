def notas(*n, sit=False):
    """
    => Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    maior = menor = 0
    for i in range(1, len(n)):
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    media = sum(n) / len(n)
    rel = dict()
    rel['total'] = len(n)
    rel['maior'] = maior
    rel['menor'] = menor
    rel['media'] = media
    if sit:
        if media >= 7:
            rel['situação'] = 'EXCELENTE!'
        elif 5 <= media < 7:
            rel['situação'] = 'BOA!'
        elif 3 <= media < 5:
            rel['situação'] = 'RUIM!'
        else:
            rel['situação'] = 'PÉSSIMA!'

    return rel


resp = notas(8, 0, sit=True)
print(resp)
