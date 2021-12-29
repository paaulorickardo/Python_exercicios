'''Escreva um programa que pergunte a qtd de km percorridos por um carro alugado e a qtd
de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$ 60,00 por dia e R$ 0,15 por km rodado'''

#Minha versão
d = float(input('Quantos dias alugados?'))
k = float(input('Qunatos km rodados? '))
print('O total a pagar é de R$ {:.2f}'.format(d * 60 + k * 0.15))
