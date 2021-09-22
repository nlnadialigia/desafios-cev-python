color = '\33[1;35m'
clear = '\33[0;0m'
vel = float(input('Digite a velocidade do carro: '))

print(color)
print('Minha Resolução: ', end='')
print(clear)
if vel > 80:
    up = vel - 80
    value = up * 7
    print('Você estava acima da velocidade permitida.')
    print('A multa é de {} por estar {}km acima do limite'.format(value, up))
else:
    print('Tudo ok. Pode prosseguir.')
