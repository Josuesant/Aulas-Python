#aula de revisão 10-12-2019

dias_do_mes ={
    1:31,
    2:28,
    3:31,
    4:31,
    5:31,
    6:31,
    7:30,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
}

qual_mes = int(input('Digite o número do mês (1...12): '))
print('O mês', qual_mes, 'tem', dias_do_mes[qual_mes], 'dias' )

print (sum(list(dias_do_mes.values())[qual_mes-1:]))