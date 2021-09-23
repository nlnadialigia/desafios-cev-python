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



