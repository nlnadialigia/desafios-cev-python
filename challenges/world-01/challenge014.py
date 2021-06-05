color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)
c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
print('A temperatura de {}°C corresponde a {}°F!' .format(c, f))
