# Faça um programa que leia a largura e altura de uma parede em metros. Calcule a sua área e a quantidade necessaria
# para pinta-lá, sabendo que cada litro de tinta, pinta uma area de 2m².
larg = float(input('Qual é a largura da parede? '))
alt = float(input('Qual é a altura da parede? '))
area = larg * alt
print('A parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('E você precisara de {}L de tinta para pintar a parede'.format(tinta))