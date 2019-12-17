# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int
from random import randint

lista1 = lista_simples_int(randint(5, 100))
lista2 = lista_simples_int(randint(5, 99))
lista3 = lista_simples_int(randint(5, 98))


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print(f'{len(lista1)} \n')

# 1.2) Qual é o maior valor da lista2?
print(f'{max(lista2)} \n')

# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
n1 = max(lista2)
n2 = min(lista2)
print(f'O maior valor da lista2 é: {n1}, e menor valor da lista2 é: {n2}, a soma desses valores é: {n1+n2} \n')

# 1.4) Qual é a média aritmética da lista1?
soma = sum(lista1)
media = len(lista1)
print(f'A média da lista1 é: {soma/media} \n')

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
print(f" Lista1 a soma é:{sum(lista1)} \n Lista2 a soma é:{sum(lista2)} \n Lista3 a soma é:{sum(lista3)} \n A soma de todas é: {sum(lista1)+sum(lista2)+sum(lista3)}")

# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
for i in lista1:
    print (f'{i} \n')

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
try:
    print(f'{lista1[5]}, {lista1[9]}, {lista1[10]}, {lista1[25]}')
    print(f'{lista2[5]}, {lista2[9]}, {lista2[10]}, {lista2[25]}')
    print(f'{lista3[5]}, {lista3[9]}, {lista3[10]}, {lista3[25]}')
except:
    print(IndexError)


# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).

if len(lista1) > len(lista2) and  len(lista1) > len(lista3):
    print(f' A lista 1 tem mais valores: {len(lista1)}')
elif len(lista2) > len(lista1) and len(lista2) > len(lista3):
    print(f'A lista 2 tem mais valores: {len(lista2)}')
else:
    print(f'A lista 3 tem mais valores: {len(lista3)}')     

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.

l1 = max(lista1)
l2 = max(lista2)
l3 = max(lista3)
soma = l1 + l2 + l3
mini = min(lista1 + lista2 + lista3)

print(f'\n A soma dos maiores números é: {soma}, subtraindo pelo menor número ({mini}) dos menores das lista o resuldato é: {soma - mini}')

# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas

soma = max(lista1 + lista2 +lista3)
mini = min(lista1 + lista2 + lista3)

print(f'\n 1O maior número das lista é: {soma}, adicionado ao menor número ({mini}) dos menor das listas o resuldato é: {soma + mini}')





