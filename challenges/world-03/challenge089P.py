from time import sleep
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução Professor: ', end='')
print(clear)
print('*' * 40)

ficha = list()
while True:
    nome = str(input('Nome: ').upper())
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('*' * 40)
print(f'{"Nº":<8}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 40)
for i, a in enumerate(ficha):
    print(f'{i:<8}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 50)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')


