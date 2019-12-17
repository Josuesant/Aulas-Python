import random

sorteado = int( random.randint(1,12) )

print('='*50)
print('\n'*3)

print(f'O numero sorteado foi: {sorteado}')
with open('0-Sorteios/alunos.txt','r') as alunos:
    contador = 1
    for i in alunos:   
        if contador == sorteado:
            print(f'Aluno : {i}')
        contador+=1 


print('\n'*3)
print('='*50)