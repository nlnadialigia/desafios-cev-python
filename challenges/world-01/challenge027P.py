color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
n = str(input('Qual é seu nome completo? ')).strip()
name = n.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(name[0].title()))
print('Seu último nome é {}'.format(name[len(name)-1].title()))

