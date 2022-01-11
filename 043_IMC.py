# Desenvolva uma logica que leia o peso e altura de uma pessoa
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
# 18.5 - Abaixo do Peso
# 18.5 e 25 - Peso idel
# 25 a 30 - Sobrepeso
# 30 até 40 Obesidade
# + que 40 Obesidade mórbita

#Versão da aula

peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)  #**2 é o mesmo que 2 ao quadrado.
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc <25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE ')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA!!')