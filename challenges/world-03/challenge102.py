def fatorial(n, show=False):
    fat = 1
    print('*' * 30)
    for i in range(1, n + 1):
        fat *= n
        if show:
            if n != 1:
                print(f'{n} x ', end='')
            else:
                print(f'{n} ', end='')
        n -= 1
    return fat


print(f'= {fatorial(5, show=True)}')
print(fatorial(5))
