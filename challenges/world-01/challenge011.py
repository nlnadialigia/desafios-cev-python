color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
wallWidth = float(input('Digite a largura da parede em metros: '))
wallHeight = float(input('Digite a altura da parede em metros: '))
area = wallHeight * wallWidth
ink = area / 2
print('Sua parede tem {:.2f}m de largura e {:.2f}m de altura,' .format(wallWidth, wallHeight), end=' ')
print('totalizando uma área de {}m2.' .format(area))
print('Para pintá-la será necessário {} litros de tinta.' .format(ink))
