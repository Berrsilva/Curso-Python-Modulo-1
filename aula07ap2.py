n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
# "print('A soma vale {}'.format(n1+n2))" ou "s = n1 + n2
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
# O {:.3f}. Serve para dizermos quantas casas iremos querer após a virgula.
# O "end=' ')" Serve para o console seguir o print na mesma linha.
print('Divisão inteira {} e potência {}'.format(di, e))