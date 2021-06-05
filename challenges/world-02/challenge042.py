color = '\33[1;35m'
clear = '\33[0;0m'

print(color)
print('Minha Resolução: ', end='')
print(clear)
print('\33[1;95m*\33[m' * 80)
print('Analisdor de Triângulos')
print('\33[1;95m*\33[m' * 80)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print('Os segmentos acima formam um Triângulo EQUILÁTERO: todos os lados são iguais')
    elif a == b and b != c:
        print('Os segmentos acima formam um Triângulo ISÓCELES: dois lados iguais e um diferente')
    else:
        print('Os segmentos acima forma um Triângulo ESCALENO: todos os lados são diferentes.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

print(color)
print('Resolução do Professor: ', end='')
print(clear)
print('\33[1;95m*\33[m' * 80)
print('Analisador de Triângulos')
print('\33[1;95m*\33[m' * 80)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
