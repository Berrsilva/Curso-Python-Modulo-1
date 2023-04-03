# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o 1º e ultimo nome separado
# Ex: Ana Maria de Souza; 1º: Ana; ultimo: Souza.
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
