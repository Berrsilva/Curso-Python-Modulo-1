na = str(input('Qual o nome do aluno? '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
m = (n1 + n2 + n3 + n4)/4
# Ou: print('A sua média foi (:.1f)',format(m))
# print ('APROVADO' if m>= 7 esle 'REPROVADO')
print ('A média do aluno {} foi de {}'.format(na,m))
if m >= 7.0:
    print('O Aluno está APROVADO!')
else:
    print('O Aluno está REPROVADO!')