from datetime import datetime


def voto():
    print(f'*' * 30)
    ano = int(input('Em que ano você nasceu? '))
    idade = datetime.now().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        resultado = 'VOTO NEGADO!'
    elif 16 <= idade < 18:
        resultado = 'VOTO OPCIONAL!'
    else:
        resultado = 'VOTO OBRIGATÓRIO!'
    return resultado


print(voto())

