def area():
    print('Controle de Terrenos'.center(30))
    print('*' * 30)
    h = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))
    print(f'A área de um terreno {h}x{b} é de {b * h}m².')


area()
