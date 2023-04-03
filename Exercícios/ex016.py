# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127. O número tem a parte inteira 6.
import math
num = float(input('Digite um número:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
# Para adicionar somente a função "trunc" basta fazer "from math import trunc". E podemos apagar o "math.trunc"
# Ou também tem a forma de somente colocar:
'''num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''