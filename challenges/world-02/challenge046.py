from time import sleep

color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('HAPPY NEW YEAR!')


