# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.


# Versão minha
# vc = float(input('Valor da casa '))
# s = float(input('Qual seu salário '))
# anos = float( input( 'Quantos anos ele vai pagar '))
# anosemmeses = anos * 12
# valorPrestacao = vc / anosemmeses
# if valorPrestacao > valorPrestacao * 30 / 100:
#     print('O valor da mensalidade será {:.2f} EMPRESTIMO NEGADO'.format(valorPrestacao))
# else:
#     print('EMPRESTIMO CONCEDIDO')

#Versão da aula

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
