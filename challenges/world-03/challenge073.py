list = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo',
        'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR',
        'Bragantino', 'Ceará', 'Corinthians', 'Atlético', 'Bahia',
        'Sport', 'Fortaleza ', 'Vasco da Gama', 'Goiás', 'Coritiba',
        'Botafogo')
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução: ', end='')
print(clear)

print('-=' * 20)
print(f'Lista de times do Brasileirão: {list}')
print('-=' * 20)
print(f'Os primeiros são: {list[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {list[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(list)}')
print('-=' * 20)
print(f'O Fluminense está na {list.index("Fluminense") + 1}ª posição')




