color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
avarage = (a + b) / 2

if avarage < 5:
    print('\33[31mSua média foi {}. Você está REPROVADO!'.format(avarage))
elif 5 < avarage < 6.9:
    print('\33[34mSua média foi {}. Você está de RECUPERAÇÃO!'.format(avarage))
else:
    print('\33[32mSua média foi {}. Você está APROVADO!'.format(avarage))

print(color)
print('Resolução do Professor: ', end='')
print(clear)
a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
avarage = (a + b) / 2
print('Tirando {:.2f} e {:.2f} a nota média do aluno é {:.2f}.'.format(a, b, avarage))

if avarage < 5:
    print('\33[31mO aluno está REPROVADO!'.format(avarage))
elif 5 <= avarage <= 6.9:
    print('\33[34mO aluno está em RECUPERAÇÃO!'.format(avarage))
else:
    print('\33[32mO aluno está APROVADO!'.format(avarage))


