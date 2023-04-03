# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário com 15% de aumento.
func = str(input('Qual o nome do funcionario? '))
sal = float(input ('Qual é o salario de {}? R$'.format(func)))
novo = sal + (sal * 15/100)
print('O salário de {} que era de R${}, com o aumento de 15% agora será de R${}'.format(func, sal, novo))