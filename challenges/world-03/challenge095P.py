jogador = {}
partidas = []
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for n in range(0, tot):
        qtde = int(input(f'     Quantos gols na partida {n+1}? '))
        partidas.append(qtde)
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-' * 60)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não exite jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i + 1} fez {g} gols')
    print()
print('<<< VOLTE SEMPRE >>>')
