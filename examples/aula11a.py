print('\033[1;31;43mOlá mundo!\033[m')

nome = 'Guanabara'
print('Olá! Muito prazer em te conhcer, {}{}{}!!!'.format('\33[1;31;47m', nome, '\33[m'))

cores = {
    'clear': '\33[m',
    'azul': '\33[34m',
    'amarelo': '\33[33m',
    'pretoebranco': '\33[7;30m'
}

print('Olá! Muito prazer em te conhcer, {}{}{}!!!'.format(cores['azul'], nome, cores['clear']))
