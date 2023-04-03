# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 20)
r1 = float(input('Primeira medida: '))
r2 = float(input('Segunda medida: '))
r3 = float(input('Terceira medida: '))
if r2 + r3 > r1 and r1 + r3 > r2 and r2 + r1 > r3:
    print('Os valores {}, {} e {} PODEM formar um triângulo!'.format(r1, r2, r3))
else:
    print('Os valores {}, {} e {} NÃO PODEM formar um triângulo!'.format(r1, r2, r3))