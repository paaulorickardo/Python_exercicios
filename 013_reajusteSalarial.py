# Faca um algoritmo que leia o salário de um funcionário e mostre seu novo salário com aumento

#Minha versão

salario = float(input('Qual o salário do funcionário? R$'))
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, salario + (salario * 15/100)))

#Sugestão na aula
vp = float(input('Valor do produto: '))
print('O valor a vista em 10% de desconto é {}, a prazo com um aumento de 8% fica no valor de R${}'.format(vp - (vp * 10/100), vp + (vp * 8/100)))
