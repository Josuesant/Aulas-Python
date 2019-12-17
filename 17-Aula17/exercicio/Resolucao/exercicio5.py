# 5.1 - Crie uma função que retorne False se a lista criada tiver alguma repetição ou tiver 
# menos que 10 númenros (números). retorne True se a lista tiver 10 números e nenhuma repetição.

# 5.2 - Crie uma lista com 100 números aleátorios. Estes números não pode ser repetidos.
# Na lista deve ter numeros de 1 a 999. Imprima na tela uma mensagem dizendo se a lista está 
# confrome a especificação ou fora de especificação.

from random import randint

def teste_lista(lista):
    if len(lista) < 10 or len(lista) > 10:
        return False
    else:
        for numero in lista:
            repeticao = lista.count(numero)
            if repeticao != 1:
                return False # o return para o ciclo dentro do def e retorna o dado sugerido.
    
    return True # se chegou até aqui é porque ele passou em todos os testes.

def teste_lista_exercicio52(lista):
    if len(lista) < 10:
        return False
    else:
        for numero in lista:
            repeticao = lista.count(numero)
            if repeticao != 1:
                return False # o return para o ciclo dentro do def e retorna o dado sugerido.
    
    return True # se chegou até aqui é porque ele passou em todos os testes.


# a = teste_lista([1,2,3,4,5,6,7,8,9,10])
# print(a)

# ### Linha 0
# lista100 = []
# aleatorio = randint(1,999)  
# lista100.append(aleatorio) # Tem que ter no minimo 1 iten na lista, senão háverá um loop infinito
# for i in range(100):
#     controle = True
#     while controle:
#         aleatorio = randint(1,999)
#         for nun in lista100:
#             if aleatorio == nun:
#                 controle = True
#                 break
#             else:
#                 controle = False
#     lista100.append(aleatorio)
# ### Linha 15   
        

                    
# a = teste_lista_exercicio52(lista100)
# lista100.sort() # serve para ordenar a lista do menor para o maior
# print(a)
# print(lista100) 


#################################################################################################################
#                       Formas alternativas
#################################################################################################################


# Esta solução é um pouco mais rápida do que a solução acima. Pois ela não verifica todos os números.
# Atentar que estou usando o metodo .sort() para ordenar a lista cada .append() novo. Isso tráz algumas
# vantagens como:
# 1 - Se o numero sorteado for menor que o primeiro ou (or) maior que o ultimo, ele entra direto.
# 2 - se o numero sorteado for igual ao numero comparado, é sorteado um outro número
# 3 - se o número não estiver na lista, mas o número é menor que o número comparado então o numero é adicionado a lista.

# ATENÇÂO! esta solução pode não ser mais rápida do que as outras a baixo dela. Mas mostra que  por mais que ela
# tenha 20 linhas é mais rápida do que a solução anterior que possui menos linhas (14 linhas).

# #### Linha 0
# lista100 = []
# aleatorio = randint(1,999)  
# lista100.append(aleatorio) # Tem que ter no minimo 1 iten na lista, senão háverá um loop infinito
# for i in range(10):
#     controle = True
#     while controle:
#         aleatorio = randint(1,999)
#         for nun in lista100:
#             if lista100[0] > aleatorio or lista100[-1] < aleatorio:
#                 controle = False
#                 break
#             elif nun == aleatorio:
#                 controle = True
#                 break
#             else:
#                 controle = False
#                 if nun > aleatorio:
#                     break               
#     lista100.append(aleatorio)
#     lista100.sort()          
# ### Linha 21        

                    
# a = teste_lista_exercicio52(lista100)
# lista100.sort() # serve para ordenar a lista do menor para o maior
# print(a)
# print(lista100) 










#################################################################################################################

# for i in range(100):
#     while True:
#         aleatorio = randint(1,999)
#         for nun in lista100:
#             if aleatorio == nun:
#                 break
#         else:  # SIM! este else é do for... caso o break não for ativado o else será executado
#             lista100.append(aleatorio)
#             break
                    
# a = teste_lista_exercicio52(lista100)
# lista100.sort()
# print(a)
# print(lista100)        
        
        
#################################################################################################################        


# for i in range(100):
#     aleatorio = randint(1,999)
#     if aleatorio in lista100:
#         while True:
#             aleatorio = randint(1,999)
#             if not aleatorio in lista100:
#                 break
#     lista100.append(aleatorio)

# a = teste_lista_exercicio52(lista100)
# lista100.sort()
# print(a)
# print(lista100)