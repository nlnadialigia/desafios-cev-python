def contador(* num):
    print(f'Recebi os valores: ', end='')
    for n in num:
        print(f'{n} ', end='')
    print()


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
