# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número qualquer: '))
if num % 2 == 0:
    print('O {} é um número PAR!'.format(num))
else:
    print('O {} é um número ÍMPAR!'.format(num))