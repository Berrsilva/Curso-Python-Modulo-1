# Escreva um programa que converta uma temperatura em Cº para Fº
tc = float(input('Informe a temperatura em Cº: '))
tf = (tc * 1.8) + 32
# ou: "tf: 9 * c / 5 +32"
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(tc, tf))
