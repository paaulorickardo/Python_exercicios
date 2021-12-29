'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na
tela.'''

#Minha versão
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e a sua porção inteira é {:.0f}.'.format(num, num))

#Versão do Professor
from math import trunc
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e a sua porça inteira é {}.'.format(num, trunc(num)))

#Versão 2
num = float(input('Digite um valor:' ))
print('O valor digitado foi {} e a sua porça inteira é {}.'.format(num, int(num)))
