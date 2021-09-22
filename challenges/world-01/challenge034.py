color = '\33[1;35m'
clear = '\33[0;0m'
salary = float(input('Qual o seu salário? R$'))

print(color)
print('Minha Resolução: ', end='')
print(clear)
if salary > 1250.00:
    a = salary + (salary * 0.10)
    print('Aumento: {}'.format(a))
else:
    a = salary + (salary * 0.15)
    print('Aumento: {}'.format(a))
