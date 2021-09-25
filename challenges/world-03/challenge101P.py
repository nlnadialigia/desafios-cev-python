# A importação dentro da função economiza memória

def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'VOTO NEGADO!'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL!'
    else:
        return 'VOTO OBRIGATÓRIO!'


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))

