jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for n in range(0, tot):
    qtde = int(input(f'     Quantos gols na partida {n+1}? '))
    partidas.append(qtde)
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'{"":>2}=> Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
