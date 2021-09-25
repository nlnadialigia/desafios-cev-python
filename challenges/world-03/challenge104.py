def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\33[1;31mERRO! Digite um número válido!\33[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
