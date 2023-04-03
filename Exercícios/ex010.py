# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos U$ ela pode comprar.
# U$1,00 = R$5,20)
real = float(input('Quantos reais você tem na carteira? R$'))
dol = real / 5.20
pesoar = real / 0.0026
print('Com seus R${:.2f} da para comprar \nU${:.2f} \nARS${:.2f}'.format(real, dol, pesoar))
