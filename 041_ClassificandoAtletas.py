# A confederação Nacional de Natação precisa de um program que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# 9 anos MIRIM, 14 INFANTIL, 19 JUNIOR, 25 SENIOR, ACIMA 25 MASTER

#Versão da aula

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

