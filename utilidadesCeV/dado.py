def leiaDinheiro(msg):
    ok =False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\33[1;31mERRO: "{n}" é um preço inválido!\33[m')
        if ok:
            break
    return valor
