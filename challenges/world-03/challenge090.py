student = dict()

student['nome'] = str(input('Nome: ')).capitalize()
student['média'] = float(input(f'Média de {student["nome"]}: '))

if student['média'] >= 6:
    student['situação'] = 'Aprovado'
else:
    student['situação'] = 'Reprovado'

for k, v in student.items():
    print(f'{k.capitalize()} é igual a {v}')
