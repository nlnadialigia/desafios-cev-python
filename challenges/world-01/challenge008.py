color = '\33[1;35m'
clear = '\33[0;0m'
n = int(input('Digite o valor em metros: '))
cm = n*100
mm = n*1000

print(color)
print('Minha Resolução: ', end='')
print(clear)
print('O valor digitado é {}m, que corresponde a {}cm e {}mm' .format(n, cm, mm))


