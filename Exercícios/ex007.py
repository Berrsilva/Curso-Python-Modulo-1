# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
a = str(input('Qual é o nome do aluno? '))
n1 = float(input('Primeira nota do {}: '.format(a)))
n2 = float(input('Segunda nota do {}: '.format(a)))
nm = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} do aluno {} foi de: {:.1f}'.format(n1, n2, a, nm))
