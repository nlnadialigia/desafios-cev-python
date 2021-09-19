import dateutil.utils

data = dict()

data['nome'] = str(input('Nome: ')).capitalize()
anoNascimento = (int(input('Ano de Nascimento: ')))
data['idade'] = dateutil.utils.today().year - anoNascimento
data['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if data['CTPS'] != 0:
    anoContratacao = int(input('Ano de contratação: '))
    data['contratação'] = anoContratacao
    data['salário'] = float(input('Salário: '))
    data['aposentadoria'] = (anoContratacao - anoNascimento) + 35

print('*' * 100)
print(data)
for k,v in data.items():
    print(f'{k} tem o valor {v}')
