# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.


controle = 's'
while controle == 's':
    try:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
        print(f' A some é: {n1+n2} \n A Subtração é: {n1-n2} \n A Multiplicação é: {n1*n2} \n A Divisão é: {n1/n2}')
        controle = input('Digite "s" para sair: ')
        if controle != 's':
                print('Continue perdendo seu tempo! ')
    
    except:
        print('Você realmente sabe o que é um numero? ')
    break    