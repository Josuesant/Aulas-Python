# Faça um programa que lê um numero inteiro do teclado e mostre a soma do numero com os 
# valores da seguinte tupla: 
# (61, 138, 13, 86, 7, 160, 150, 90, 182, 158, 167, 171, 79, 162, 197, 63, 164, 22, 194, 17, 168)
# use o f-string para apresentar o numero.


tupla = (61, 138, 13, 86, 7, 160, 150, 90, 182, 158, 167, 171, 79, 162, 197, 63, 164, 22, 194, 17, 168)
numero = int(input('Digite um número inteiro: '))

for numero_tupla in tupla:
    print(f'{numero} + {numero_tupla}   =   {numero + numero_tupla}')
