def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except Exception as error:
            # print('\33[31mUsuário preferiu não digitar esse número.\33[m')
            print('ERRO: por favor, digite um número inteiro válido')
        else:
            break
    return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except Exception as error:
            print('ERRO: por favor digite um número real válido')
        else:
            break
    return n


# Programa principal
i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
