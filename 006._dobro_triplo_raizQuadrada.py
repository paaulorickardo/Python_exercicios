# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

#Minha versão
from math import sqrt

a = int(input('Digite um número: '))
d = a * 2
t = a * 3
r = sqrt(a)
print('O dobro do número {}'.format(d))
print('O triplo do número {}'.format(t))
print('A raiz quadrada do número {}'.format(r))

#Versão da aula

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.\n A raiz quadrada de {} é igual a {:.2f}'.format(n, t, n, r))

#Versão 2
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n * 2)))
print('O triplo de {} vale {}.\n A raiz quadrada de {} é igual a {:.2f}'.format(n, (n * 3), n, pow(n, (1/2))))
