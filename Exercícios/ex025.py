# Crie um programa que leia o nome da pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))