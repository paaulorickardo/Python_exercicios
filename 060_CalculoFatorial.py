# Faça um programa que leia um numero qualquer e mostre seu fatorial
# Ex: 5! 5*4*3*2*1 = 120


#Versão da aula
#Ultilizando modulo
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

# Padrão
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f))
