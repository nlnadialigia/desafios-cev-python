color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
salary = float(input('Digite o valor do seu salário: '))
increase = 15
newSalary = salary + (salary * (increase/100))
print('Seu salário passou de R${:.2f} para R${:.2f}' .format(salary, newSalary), end=' ')
print('devido a um reajuste de {}%' .format(increase))

print(color)
print('Resolução do Professor: ', end='')
print(clear)
salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario * 0.15)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, \npassa a receber R${:.2f}!' .format(salario, novo))

