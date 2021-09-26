# RESOLUÇÃO DO PROFESSOR
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO: por favor, digite um número inteiro válido\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[31mUsuário preferiu não digitar esse número.\33[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor digite um número real válido')
            continue
        except KeyboardInterrupt:
            print('\n\33[31mUsuário preferiu não digitar esse número.\33[m')
            return 0
        else:
            return n


# Programa principal
i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
