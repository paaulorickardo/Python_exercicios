


#Minha versão

# salario = float(input('Qual o sário do funcionário ? R$'))
# if salario <= 900:
#     quinze = salario + (salario * 15 / 100)
#     print('Quem ganhava R$ {} passa a ganhar R$ {} agora.'.format(salario, quinze))
# else:
#     dez = salario(salario * 10 / 100)
# print('Quem ganhava R$ {} passa a ganhar R$ {}agora.'.format(salario, dez))

#Versão aula
salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))
