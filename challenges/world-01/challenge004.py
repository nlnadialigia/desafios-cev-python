msg = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(msg))
print('Só tem espaço?', msg.isspace())
print('É um número?', msg.isnumeric())
print('É alfabético?', msg.isalpha())
print('É alfa-numérico?', msg.isalnum())
print('Está em maiúsculas?', msg.isupper())
print('Está em minúsculas?', msg.islower())
print('Está capitalizada?', msg.isupper())
