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

print(color)
print('Resolução do Professor: ', end='')
print(clear)
sexo = str(input('Informe seu sexo: [M/F] => ')).strip().upper()[0]
while sexo not in 'MmFf':
   print('Dados inválidos!', end=' ')
   sexo = str(input('Por favor digite seu sexo: [M/F] => ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
