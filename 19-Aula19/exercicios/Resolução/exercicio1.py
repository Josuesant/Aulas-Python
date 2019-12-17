# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]

#  [
# 0    'nome'                                                                     0 #
# 1  '['Alex'   , 'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],   1 #
# 2    'telefone',                                                                2 #
# 3  '['4799991', '4799992','4799993','4799994','4799995','4799996','4799997'],   3 #
# 4    'email',                                                                   4 #
# 5  '['a@a.com', 'b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],   5 #
# 6    'idade',                                                                   6 #
# 7  '['18'     , '25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]]   7 #
#
#       0          1         2         3         4         5         6




# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com


print(f'{cadastroHBSIS[0]}  {cadastroHBSIS[1][0]} {cadastroHBSIS[2]}: {cadastroHBSIS[3][0]}')
print(f'{cadastroHBSIS[6]}  {cadastroHBSIS[1][4]} {cadastroHBSIS[7][4]} anos')
print(f'{cadastroHBSIS[4]} de {cadastroHBSIS[1][3]} é {cadastroHBSIS[5][3]}')


dicionário {cadastroHBSIS[0]: 'valor'}


#  [
# 0    'nome'                                                                     0 #
# 1  '['Alex'   , 'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],   1 #
# 2    'telefone',                                                                2 #
# 3  '['4799991', '4799992','4799993','4799994','4799995','4799996','4799997'],   3 #
# 4    'email',                                                                   4 #
# 5  '['a@a.com', 'b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],   5 #
# 6    'idade',                                                                   6 #
# 7  '['18'     , '25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]]   7 #
#
#       0          1         2         3         4         5         6


# 2 - usando o for, imprima todos nomes um abaixo do outro
#

for nome in cadastroHBSIS[1]:
    print(nome)



# 3 - Usando a indexação faça uma lista com 3 bibliotecas contendo os dados 
# do Mateus, Paulo # e João contendo
# como chaves: nome, email, idade, telefone (nesta  sequencia)

lista = [
{'nome'           : cadastroHBSIS[1][3], 'email'          : cadastroHBSIS[5][3], 'idade'          : cadastroHBSIS[7][3], 'telefone'       : cadastroHBSIS[3][3]},
{cadastroHBSIS[0] : cadastroHBSIS[1][1], cadastroHBSIS[4] : cadastroHBSIS[5][1], cadastroHBSIS[6] : cadastroHBSIS[7][1], cadastroHBSIS[2] : cadastroHBSIS[3][1]},
{cadastroHBSIS[0] : cadastroHBSIS[1][5], cadastroHBSIS[4] : cadastroHBSIS[5][5], cadastroHBSIS[6] : cadastroHBSIS[7][5], cadastroHBSIS[2] : cadastroHBSIS[3][5]}
        ]

for i in lista:
    print(i)


#  [
# 0    'nome'                                                                     0 #
# 1  '['Alex'   , 'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],   1 #
# 2    'telefone',                                                                2 #
# 3  '['4799991', '4799992','4799993','4799994','4799995','4799996','4799997'],   3 #
# 4    'email',                                                                   4 #
# 5  '['a@a.com', 'b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],   5 #
# 6    'idade',                                                                   6 #
# 7  '['18'     , '25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]]   7 #
#
#       0          1         2         3         4         5         6

