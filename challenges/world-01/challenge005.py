"""Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor"""
n = int(input('Digite um número: '))

print('Minha resolução:')
print('O número é: {}' .format(n))
print('Seu sucessor é o número {}' .format(n+1))
print('Seu antecessor é o número {}' .format(n-1))

print("*" * 80)

print('Resolução do professor:')
a = n - 1
s = n + 1
print('Analisando o valor {}, seu sucessor é {} e seu antecessor é {}' .format(n, s, a))

