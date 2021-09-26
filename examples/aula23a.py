try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as error:
    print(f'Problema encontrado foi \33[31m{error.__class__}\33[m')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado')

