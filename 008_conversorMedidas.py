'''Escreva um programa que leia um valor em metros e o exiba convertido em
centimetros.  ESCALA km hm dam m dm cm mm '''

# Versão da aula

medidas = float(input('Uma distancia em metros: '))
km = medidas / 1000
hm = medidas / 100
dam = medidas / 10
dm = medidas * 10
cm = medidas * 100
mm = medidas * 1000
print('A medida de {}m corresponde a \n {:.0f}cm \n {:.0f}dm, \n {:.2f}hm, \n {:.3f}km'.format(medidas, cm, mm, dm , dam, hm, km))
