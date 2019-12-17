# Aula 20 - 05-12-2019
# Lista com for e metodos

# Com esta lista:

lista = [
         ['codigo','produto','valor','quantidade'],
         [1,'Cevada',15.00,10],
         [2,'Lupulo',150.50,200],
         [3,'Malte',57.80,5000],
         [4,'Levedura 1',10.65,500],
         [5,'Extrato de Levedura',15.00,60],
         [6,'Levedura 2',15.50,87]
        ]




# 2.1 - Faça uma função que pegue esta lista e retorne uma lista com biblioteca.

# 2.2 - Faça outra função para consultar o preço através do código passado
# por parametro. Esta função deve printar o nome do produto, a quantidade
# e o preço.
# Execute esta função dentro do while e quando digitar qualquer código que 
# não tenha produto cadastrado o programa se encerra.
#

# ###############Procurar e reconhecer padrão!

#   lista[0][0] : lista[1][0]  codigo : 1
#   lista[0][1] : lista[1][1]  produto : cevada
#   lista[0][2] : lista[1][2]  valor : 15.00
#   lista[0][3] : lista[1][3]  quantidade : 10

#   lista[0][0] : lista[2][0]  codigo : 2
#   lista[0][1] : lista[2][1]  produto : lupulo
#   lista[0][2] : lista[2][2]  valor : 150.50
#   lista[0][3] : lista[2][3]  quantidade : 200

#   lista[0][rapido] : lista[lento][rapido]

# ################################################


def lista_biblioteca(lista):
        lista_bibl = []
        for lento in range ( len(lista[1:]) ):
                biblioteca = {}
                for rapido in range( len(lista[0]) ):
                        biblioteca[ lista[0][rapido]] = lista[lento+1][rapido]
                lista_bibl.append(biblioteca)
        return lista_bibl

def consulta(lista,codigo):
        for produto in lista:
                if int(produto['codigo']) == codigo:
                        print(f"\nNome do produto: {produto['produto']}\n"
                              f"Quantidade em estoque: {produto['quantidade']}\n"
                              f"Preço: R$ {produto['valor']:.2f}\n")
                        return True
        return False
                        


lista1 = lista_biblioteca(lista)

sair = True
while sair:
        codigo = int(input('Digite o código produto: '))
        sair = consulta(lista1,codigo)