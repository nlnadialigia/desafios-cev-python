from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome: ')).capitalize()
anoNascimento = (int(input('Ano de Nascimento: ')))
dados['idade'] = datetime.now().year - anoNascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    anoContratacao = int(input('Ano de contratação: '))
    dados['contratação'] = anoContratacao
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('-=' * 100)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
