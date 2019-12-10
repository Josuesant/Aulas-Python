from calc2 import *

valor = float(input('\nDigite o valor que será poupado: '))
rent = float(input('\nDigite a rentabilidade: '))
rent = rent/100
valor_mes = calc_mes(valor, rent)
valor_ano = calc_ano(valor, rent)

print(f'''\n
A rentabilidade aplicada foi de: {rent*100}% \n
O lucro por mês será de: {valor_mes} \n
O lucro por ano será de: {valor_ano:0.2f}\n'''
)