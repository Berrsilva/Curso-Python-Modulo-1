# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
# 0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
cid = str(input('Para qual cidade você deseja viajar? '))
dist = float(input('Distância em KM da viagem: '))
print('Sua viagem para {} será de {}KM'.format(cid, dist))
if dist <= 200:
    valor = (dist * 0.5)
else:
    valor = (dist * 0.45)
print('Na distância de {}KM. O preço por KM fica R$0,45. O valor total é de: R${:.2f}'.format(dist, valor))