
''''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa'''

#Versão aula
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#Versão 2
from math import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
