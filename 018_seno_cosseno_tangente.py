'''Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse angulo'''

#Versão da aula

from math import radians, sin, cos, tan

ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO DE {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

