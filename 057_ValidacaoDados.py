# Faca um programa que leia o sexo de uma pessoa, mas só aceitte os  valores
# M ou F. Caso esteja errado peça a digitação novamente até ter um valor correto.

#Versao da aula
sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos.Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
