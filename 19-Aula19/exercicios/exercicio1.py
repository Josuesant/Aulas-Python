# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]


# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com


# 2 - usando o for, imprima todos nomes um abaixo do outro
#
# 3 - Usando a indexação faça uma lista com 3 dicionários contendo os dados 
# do Mateus, Paulo # e João contendo
# como chaves: nome, email, idade, telefone (nesta  sequencia)

campos = cadastroHBSIS[0::2]
dados = cadastroHBSIS[1::2]

lista = [{}, {}, {}]

contador_campo = 0
for i in dados:
    lista_dados = i [1::2]
    contador =0

    for lista_campos in lista_dados:
        dic = lista[contador]
        dic[campos[contador_campo]] = lista_campos
        contador +=1

    contador_campo +=1

for j in lista:
    print(j)    
