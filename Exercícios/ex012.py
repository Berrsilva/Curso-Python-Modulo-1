# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Qual o preço deste produto? R$'))
novo = preco - (preco * 5/100)
print ('O preço que custava R${:.2f}, na promoção de 5% ele custara R${:.2f}'.format(preco, novo))