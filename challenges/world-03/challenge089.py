from time import sleep
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)

list = list()
student = ''
while True:
    name = str(input('Nome: ')).strip()
    note_one = float(input('Nota 1: '))
    note_two = float(input('Nota 2: '))
    avarage = (note_one + note_two) / 2
    list.append([name, [note_one, note_two], avarage])
    choice = input('Quer continuar? [S/N] ').upper()
    if choice == 'N':
        break
print('-=' * 40)
print(list)
print('Nº'.ljust(10), end='')
print('NOME'.ljust(20), end='')
print('MÉDIA')
print('*' * 40)
for n in range(0, len(list)):
    print(f'{n}'.ljust(10), end='')
    print(f'{list[n][0]}'.ljust(20), end='')
    print(f'{list[n][2]}')
print('*' * 40)

while True:
    student = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if 0 <= student <= len(list)-1:
        print(f'Notas de {list[student][0]} são: {list[student][1]}')
    elif student == 999:
        break
    else:
        print('Aluno não encontrado!')
    print('*' * 40)
print('FINALIZANDO...')
sleep(1)
print('<<<< VOLTE SEMPRE >>>>')
