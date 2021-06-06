color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução: ', end='')
print(clear)
words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in words:
    print(f'Na palavra {c.upper()} temos ', end='')
    for x in c.lower():
        if x in 'aeiou':
            print(x, end=' ')
    print('')
