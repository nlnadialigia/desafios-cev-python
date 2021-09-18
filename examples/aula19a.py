pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['peso'] = 98.5

print(pessoas)

del pessoas['idade']
print(pessoas)