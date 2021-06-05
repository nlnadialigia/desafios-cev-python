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

print(color)
print('Resolução do Professor: ', end='')
print(clear)
vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80kmm/h')
    value = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(value))
print('Tenha um bom dia! Dirija com segurança!')

