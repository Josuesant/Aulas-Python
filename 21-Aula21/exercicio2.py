# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# DICA!  O comando range() funciona de 3 formas diferentes, uma para
# cada situação.
# range(10) - Com a passagem de um único número o range irá começar 
# a contar do 0 até 9
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# range(1,10) - Com a passagem de um 2 números o range irá começar 
# a contar do 1 até 9. Lembrando que o número 10 não aparece na contagem.
# 1, 2, 3, 4, 5, 6, 7, 8, 9,

# range(1,10,2) - Com a passagem do 3 número o range irá começa do 1
# até o 9 contando de 2 em 2 
# 1, 3, 5, 7, 9.

# para criar uma lista com o range() basta converte-lo em uma lista
# Ex:  a = range(2,30,3) > [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]

#####################################################################

# 1 - Crie um programa que leia 5 números inteiros, salve-os em uma
# lista e faça a média deles.
# 
# Use o for e o range() para isso.
#
# Caso um dado que não seja inteiro for digitado, deverá aparecer uma
# mensagem dizendo "Erro! Digite numeor inteiro!"
#
# Imprima o valor

lista =[]
controle = 's'
while controle == 's':
    try:
        n1 = int(input('Digite 0 1° numero: '))
        n2 = int(input('Digite 0 2° numero: '))
        n3 = int(input('Digite 0 3° numero: '))
        n4 = int(input('Digite 0 4° numero: '))
        n5 = int(input('Digite 0 5° numero: '))


    except ValueError:
         print('Erro! Digite numero inteiro! ')
    
    else:
        lista = [n1, n2, n3, n4, n5]
        media = sum(lista) / len(lista)

        print(f'A média dos 5 numeros é: {media} ')
        controle = input('Digite "s" para sair: ')
     
        if controle == 's':
             break
        else:
            print('Continue fazendo seu calculos!')   
            continue
             