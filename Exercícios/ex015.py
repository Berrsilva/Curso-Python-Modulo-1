# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado
dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))
vt = (dias * 60) + (km * 0.15)
print('O valor total com {} dias alugados e {} andados fica R${:.2f}!'.format(dias, km, vt))