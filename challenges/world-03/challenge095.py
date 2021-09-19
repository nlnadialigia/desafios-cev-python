data = {}
jogadores = []

while True:
    total = 0
    lista_gols = []
    data['nome'] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {data["nome"]} jogou? '))
    for n in range(0, partidas):
        qtde = int(input(f'Quantos gols na partida {n+1}? '))
        lista_gols.append(qtde)
    data['gols'] = lista_gols
    for i in lista_gols:
        total += i
    data['total'] = total
    jogadores.append(data.copy())
    data.clear()

    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'S':
        print('-' * 40)
    else:
        print('-=' * 30)
        break
print(jogadores)

# jogadores = [
#     {'nome': 'Ana', 'gols': [1, 1], 'total': 2},
#     {'nome': 'Pedro', 'gols': [1, 2, 0], 'total': 3},
#     {'nome': 'Eduardo', 'gols': [0, 2, 7], 'total': 9}
# ]

print(f'{"cod":<10}{"nome":<20}{"gols"}{"":<15}{"total":>4}')
print('-' * 70)

for n in range(0, len(jogadores)):
    x = jogadores[n]
    print(f"{n:<10}{x['nome']:<20}{x['gols']}{'':<15}{x['total']:<4}")
    print()

while True:
    print('-' * 70)
    ask = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if ask == 999:
        break
    if ask >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {ask}! Tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[ask]["nome"]}: ')
        for n in range(0, len(jogadores[ask]['gols'])):
            print(f'No jogo {n + 1} fez {jogadores[ask]["gols"][n]}.')
print(("-" * 70))
