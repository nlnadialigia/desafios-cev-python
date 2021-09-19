data = {}
lista_gols = []
total = 0

data['nome'] = str(input('Nome do Jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas {data["nome"]} jogou? '))
for n in range(0, partidas):
    qtde = int(input(f'Quantos gols na partida {n+1}? '))
    lista_gols.append(qtde)
data['gols'] = lista_gols

for i in lista_gols:
    total += i
data['total'] = total

print('-=' * 30)
print(data)
for k, v in data.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

if partidas == 0:
    print(f'O jogador {data["nome"]} não jogou nenhum partida.')
else:
    print(f'O jogador {data["nome"]} jogou {len(lista_gols)} partidas.')
    if total == 0:
        print('O jogador não fez gols.')
    else:
        for n in range(0, len(data['gols'])):
            print(f'{"":>2}=> Na partida {n + 1}, fez {lista_gols[n]} gols.')
        print(f'Foi um total de {data["total"]} gols.')
