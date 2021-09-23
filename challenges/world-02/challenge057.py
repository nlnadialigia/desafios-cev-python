color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
sexo = str(input('Digte o sexo: [M/F] => ')).upper()
while sexo != 'M' and sexo != 'F':
   print('Resposta incorreta. Digite novamente!')
   sexo = str(input('Digte o sexo: [M/F] => ')).upper()
print('FIM')

