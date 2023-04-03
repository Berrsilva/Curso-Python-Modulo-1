# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.
import random
from time import sleep
print('-=-' * 20)
print('Vou escolher um número entre 0 e 5, tente advinhar...')
print('-=-' * 20)
na = random.randint(0, 5)
r =int(input('Tente advinhar o número: '))
print('PROCESSANDO...')
sleep(2)
if r == na:
    print('Parabéns, você advinhou, como conseguiu ler a minha mente?')
else:
    print('Não foi dessa vez, Eu pensei no número {} e não no {}!'.format(na, r))