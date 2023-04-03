# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas. (FEITO)
# O nome com todas as letras minusculas. (FEITO)
# Quantas lestras tem ao todo (sem considerar espaço). (FEITO)
# Quantas letras tem o primeiro nome. (FEITO)

nome = str(input('Digite o seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúscula é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))