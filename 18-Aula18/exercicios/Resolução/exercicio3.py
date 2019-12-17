# Aula 18 - 03-12-2019

# A lista a seguir possui mais uma lista interna, a lista de preços.
# A lista de preços possui 3 sublistas dentro dela com os preços dos produtos.
# para exemplificar, o preço do mamão é de 10.00 - alface crespa é de 2.99 e o feijão 9.0

lista = [['frutas','verduras','legumes','preço'],
         ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
         ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha','cebolinha'],
         ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
         [ [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
           [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] 
         ]
        ]



# {lista[][]}
# 0   ['frutas',        'verduras',   'legumes'],                                                      0   #
# 1   ['mamão',         'abacaxi',    'laranja', 'uva',    'pera',         'maçã',       'vergamota'], 1   #
# 2   ['alface crespa', 'alface lisa','rucula','  almerão','repolho',      'salsinha',   'cebolinha'], 2   #
# 3   ['feijão',        'erviha',     'lentilha','vagem',  'feijão branco','gão de bico','soja']       3   #

# {lista[][][]}
# 4 0 [ 10.00,           2.56,         5.25,      9.5,      10.05,          15,           5.75]        4 0 #
# 4 1 [ 2.99,            2.95,         3.5,       3.25,     5.89,           2.9,          2.5],        4 1 #
# 4 2 [ 9.0,             5.0,          7.5,       1.75,     10.9,           5.99,         3.55]        4 2 #

#       0                 1              2        3           4               5            6



# {lista[][]} {lista[][][]}
# 0   ['frutas',        'verduras',   'legumes'],                                                      0   #
# 1   ['mamão',         'abacaxi',    'laranja', 'uva',    'pera',         'maçã',       'vergamota'], 1   #
# 4 0 [ 10.00,           2.56,         5.25,      9.5,      10.05,          15,           5.75]        4 0 #
# 2   ['alface crespa', 'alface lisa','rucula','  almerão','repolho',      'salsinha',   'cebolinha'], 2   #
# 4 1 [ 2.99,            2.95,         3.5,       3.25,     5.89,           2.9,          2.5],        4 1 #
# 3   ['feijão',        'erviha',     'lentilha','vagem',  'feijão branco','gão de bico','soja']       3   #
# 4 2 [ 9.0,             5.0,          7.5,       1.75,     10.9,           5.99,         3.55]        4 2 #

#       0                 1              2        3           4               5            6




# Será solicitado o preço de alguns produtos. para imprimir deve ser por f-string refrenciando o nome com o preço 
# da seguinte forma: "O preço do {} é R$ {}"

print('1: imprima o valor do abacaxi')
print(f'{lista[1][1]} = R$ {lista[4][0][1]:.2f}')

print('2: imprima o valor da rucula')
print(f'{lista[2][2]} = R$ {lista[4][1][2]:.2f}')

print('3: imprima o valor da laranja')
print(f'{lista[1][2]} = R$ {lista[4][0][2]:.2f}')

print('4: imprima o valor do repolho')
print(f'{lista[2][4]} = R$ {lista[4][1][4]:.2f}')

print('5: imprima o valor do feijão')
print(f'{lista[3][0]} = R$ {lista[4][2][0]:.2f}')

print('6: imprima o valor do feijão branco')
print(f'{lista[3][4]} = R$ {lista[4][2][4]:.2f}')

print('7: imprima o valor da vergamota')
print(f'{lista[1][6]} = R$ {lista[4][0][6]:.2f}')

print('8: imprima o valor da alface lisa')
print(f'{lista[2][1]} = R$ {lista[4][1][1]:.2f}')

print('9: imprima o valor do mamão')
print(f'{lista[1][0]} = R$ {lista[4][0][0]:.2f}')

print('10: imprima o valor da soja')
print(f'{lista[3][6]} = R$ {lista[4][2][6]:.2f}')

print('11: imprima o valor da lentilha')
print(f'{lista[3][2]} = R$ {lista[4][2][2]:.2f}')

print('12: imprima o valor da uva')
print(f'{lista[1][3]} = R$ {lista[4][0][3]:.2f}')

print('13: imprima o valor da vagem')
print(f'{lista[3][3]} = R$ {lista[4][2][3]:.2f}')

print('14: imprima o valor do almerão')
print(f'{lista[2][3]} = R$ {lista[4][1][3]:.2f}')

print('15: imprima o valor da ervilha')
print(f'{lista[3][1]} = R$ {lista[4][2][1]:.2f}')

print('16: imprima o valor da maçã')
print(f'{lista[1][5]} = R$ {lista[4][0][5]:.2f}')



# print(f'{lista[][]} = R$ {lista[][][]:.2f}')
# 0   ['frutas',        'verduras',   'legumes'],                                                      0   #
# 1   ['mamão',         'abacaxi',    'laranja', 'uva',    'pera',         'maçã',       'vergamota'], 1   #
# 4 0 [ 10.00,           2.56,         5.25,      9.5,      10.05,          15,           5.75]        4 0 #
# 2   ['alface crespa', 'alface lisa','rucula','  almerão','repolho',      'salsinha',   'cebolinha'], 2   #
# 4 1 [ 2.99,            2.95,         3.5,       3.25,     5.89,           2.9,          2.5],        4 1 #
# 3   ['feijão',        'ervilha',     'lentilha','vagem',  'feijão branco','gão de bico','soja']       3   #
# 4 2 [ 9.0,             5.0,          7.5,       1.75,     10.9,           5.99,         3.55]        4 2 #

#       0                 1              2        3           4               5            6



