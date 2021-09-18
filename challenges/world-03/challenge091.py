from random import randint

players = dict()
lista = dict()

print('*' * 30)
print('Valores sorteados:')
for n in range(0, 4):
    players['jogador'] = n + 1
    players['numero'] = randint(1, 6)
    print(f'O jogador{players["jogador"]} tirou {players["numero"]}')
    lista[f'{n+1}'] = players.copy()

# lista = {
#     '1': {'jogador': 1, 'numero': 2},
#     '2': {'jogador': 2, 'numero': 6},
#     '3': {'jogador': 3, 'numero': 5},
#     '4': {'jogador': 4, 'numero': 3}
# }




