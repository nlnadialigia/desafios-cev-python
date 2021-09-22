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


