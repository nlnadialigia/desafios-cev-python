data = {}
lista = []
soma = 0

while True:
    data['nome'] = str(input('Nome: ')).capitalize()
    data['sexo'] = str(input('Sexo: [M/F] ')).upper()
    data['idade'] = int(input('Idade: '))
    soma += data['idade']
    lista.append(data.copy())
    data.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'N':
        break
print('-=' * 50)
print(f'- O grupo tem {len(lista)} pessoas.')
media = soma / len(lista)
print(f'- A média de idade é de {media} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for n in range(0, len(lista)):
    if lista[n]['sexo'] == 'F':
        print(f'{lista[n]["nome"]} ', end='')
print()
print(f'- Lista das pessoas que estão acima da média:')
for n in range(0, len(lista)):
    for k, v in lista[n].items():
        if lista[n]['idade'] > media:
            print(f'{k} = {v}; ', end='')
    print()
print('<< ENCERRADO >>')
