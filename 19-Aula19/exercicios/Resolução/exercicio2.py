# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
#
#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())
#
#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)



cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
        ]

# cab[0] pess[0][0]  #nome        alex
# cab[1] pess[1][0]  #telefone    4799991
# cab[2] pess[2][0]  #email       a@a.com
# cab[3] pess[3][0]  #idade       18

# cab[0] pess[0][1]  #nome        Paulo
# cab[1] pess[1][1]  #telefone    4799992
# cab[2] pess[2][1]  #email       b@b.com
# cab[3] pess[3][1]  #idade       25

lista = []

for indice_lento in range(7):
        dic = {}
        for indice_rapido in range(4):
                
                dic[ cab[ indice_rapido ] ] = pess[ indice_rapido ][ indice_lento ]
                
        lista.append(dic)

for i in lista:
        print(i)

















