#--- Exercício 2 - Dicionários
#--- Escreva um programa que leia os dados de 11 jogadores
#--- Jogador: Nome, Posicao, Numero, PernaBoa
#--- Crie um dicionario para armazenar os dados
#--- Imprima todos os jogadores e seus dados

#--- Resolução Nicole Gruber

lista_jogadores=[]
for i in range(1,3):
    Nome=input('Digite o nome do jogador: ')
    Posicao=input('Digite a posiçao do jogador: ')
    Numero=input('Digite o numero do jogador: ')
    PernaBoa=input('Digite a Perna Boa do jogador: ')

    dicionario = {'Nome': Nome, 'Posicao': Posicao, 'Numero': Numero, 'PernaBoa': PernaBoa}

    lista_jogadores.append(dicionario)

for dicionario in lista_jogadores:
    print(f"Nome={dicionario['Nome']}, Posiçao={dicionario['Posicao']}, Numero={dicionario['Numero']}, PernaBoa {dicionario['PernaBoa']}")