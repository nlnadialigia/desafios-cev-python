from time import sleep


def maior(*num):
    print('-=' * 40)
    print('Analisando os valores passados...')
    sleep(1)
    if len(num) == 0:
        print('Não foram informados valores')
    else:
        m = num[0]
        for n in num:
            print(f'{n} ', end='')
            if n > m:
                m = n
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {m}')
    print('-=' * 40)


maior(2, 9, 4, 5, 7, 1)
sleep(1)
maior(4, 7, 0)
maior()
