color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80kmm/h')
    value = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(value))
print('Tenha um bom dia! Dirija com segurança!')

