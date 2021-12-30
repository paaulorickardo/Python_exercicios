'''Faça um program que leia um número de 0 a 9999 e mostre na tela cada um dos
dígitos separados'''

#Versão professor
num = str(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

#versão ruim começa a dar erro dependendo do número
#Versão 2 correta

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Cetena: {}'.format(c))
print('Milhar: {}'.format(m))
