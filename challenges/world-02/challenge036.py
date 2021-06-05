color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
house = float(input('\33[33mQual o valor da casa? R$'))
salary = float(input('\33[34mQual é o seu salário? R$'))
years = int(input('\33[35mEm quantos anos pretende pagar? '))

payment = house / (years * 12)
print('payment: R${:.2f}'.format(payment))

if salary * 0.30 < payment:
    print('Seu empréstimo foi negado! O valor da sua parcela não deve ser maior que R${:.2f}'.format(salary * 0.30))
else:
    print('Parabéns! Seu empréstimo foi aprovado! Sua parcela mensal será de R${:.2f}'.format(payment))

print(color)
print('Resolução do Professor: ', end='')
print(clear)
house = float(input('\33[33mValor da casa: R$'))
salary = float(input('\33[34mSalário do comprador: R$'))
years = int(input('\33[35mQuantos anos de financiamento? \33[m'))

payment = house / (years * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(house, years, payment))

if salary * 0.30 <= payment:
    print('Seu empréstimo foi NEGADO! O valor da sua parcela não deve ser maior que R${:.2f}'.format(salary * 0.30))
else:
    print('Parabéns! Seu empréstimo foi APROVADO! Sua parcela mensal será de R${:.2f}'.format(payment))
