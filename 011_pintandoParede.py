'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a qtd de tinta necessária para pintá-la, dabendo que cada litro de tinta
pinta uma área de 2 m2'''

#Minha versão
l = float(input('Largura de parede: '))
a = float(input('Altura da parede '))
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m2.'.format(l, a, l * a))
print('Para pintar sua parede, você precisará de {}l de tinta'.format((l * a)/2))

#Versão da aula bem parecida