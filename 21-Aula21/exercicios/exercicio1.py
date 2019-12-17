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

controle = 'n'
while controle != 's':
    numero1 = int(input('Digite o número 1: '))
    numero2 = int(input('Digite o número 2: '))

    print(f'A soma de {numero1} e {numero2} é: {numero1 + numero2}')
    print(f'A divisão de {numero1} e {numero2} é: {numero1 / numero2}')
    print(f'A multiplicação de {numero1} e {numero2} é: {numero1 * numero2}')
    print(f'A subtração de {numero1} e {numero2} é: {numero1 - numero1}')

    controle = input("Digite 's' para sair: ")


# try:
#     numero = int(input('Digite um numero:'))
# except:
#     print('Voce digitou o numero errado animal!')

# print('1')
# print('2')
# while True:

#     try:
#         n=0
#         while True:
#             print(n)
#             n+=1
#     except:
#         print('ferrou!')



while True:
    try:
        print('Passou 1')
        numero = int(input('Digite um numero1:'))
        numero2 = int(input('Digite um numero2:'))

        print(numero/numero2)
        print('Passou 2')

    except (ValueError,ZeroDivisionError):
        print('Voce digitou ALGO errado CEU!!! animaUUU!')

    # except ZeroDivisionError:
    #     print('Voce dividiu por zero')

    else:
        print('FIM!')
        break

        
