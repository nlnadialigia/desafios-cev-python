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

