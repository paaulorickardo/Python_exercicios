# Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#Versão minha
from time import sleep
# print(0)
# sleep (1)
# print(1)
# sleep(1)
# print(2)
# sleep(1)
# print(3)
# sleep(1)
# print(4)
# sleep(1)
# print(5)
# sleep(1)
# print(6)
# sleep(1)
# print(7)
# sleep(1)
# print(8)
# sleep(1)
# print(9)
# sleep(1)
# print(10)

#Versão da aula

for cont in range(10, -1, -1): # os -1 são para incluir o zero OU ultimo termo
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOW!')
