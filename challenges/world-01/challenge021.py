from pygame import mixer
color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Resolução do Professor: ', end='')
print(clear)

mixer.init()
mixer.music.load('midia.mp3')
mixer.music.play()
x = input('digite algo para encerrar ...')


