#--- Lista de passageiros que estão no terminal, e lista de avião vazia, pronta para receber os passageiros.
from revisao2 import *
aviao = []
terminal = txt_terminal()
#--- Logica;/Função para mostrar/retornar a logistica de como os passageiros vão embar no avião. 
def transporte():                

    if not terminal:
        return ('Todos os passageiros já embarcaram! ')            
    elif terminal[0] == 'Presidiário' or terminal[0] == 'Policial':
        return (f'O {terminal[0]} está sendo transportado pelo {terminal[1]}')
    elif terminal[0] == 'Chefe' and terminal[1] != 'Piloto':
        return(f'O {terminal[1]} está sendo transportado pelo Chefe')
    elif terminal[0] == 'Chefe':
        return(f'O {terminal[0]} está sendo transportado pelo {terminal[1]}')
    elif terminal[0] == 'Piloto' and terminal[len(terminal)-1] != 'Piloto':
        return(f'A {terminal[1]} está sendo transportado pelo {terminal[0]}')

#--- Função que mostra o menu, onde as informações serão atualizadas a cada ENTER        
def menu():
    print (f'''
                ###############################################################
                
                Passageiros para Embarque: {terminal}
                {transporte()}
                Passageiros Embarcados no Avião: {aviao}                              
                        
                ###############################################################\n''')

menu()

#--- Logica/Função que recebe como parâmetro as listas, a ao remover acada item de uma vai adicionando a outra,onde também são
#  aplicadas as condições/regras de transporte. A dinâmica muda quando ficam apenas dois elementos na lista, neste caso os dois
#  são removidas do terminal e addicionados ao avião. 
def mostrar(terminal,aviao):
    try: 
        while terminal.count != 0:
            a = input(f'\n Precione ENTER para continuar')
            
            if a == '':
                if terminal[0] == 'Chefe' and terminal[len(terminal)-1] != 'Chefe' and terminal[1]== 'Comissária2':
                    pas = terminal.pop(1)
                    aviao.append(pas)
                    pas = terminal.pop(0)
                    aviao.append(pas)
                    menu()

                elif terminal[0] == 'Chefe' and terminal[len(terminal)-1] != 'Chefe':
                    pas = terminal.pop(1)
                    aviao.append(pas)
                    menu()    

                elif terminal[0] == 'Piloto' and terminal[1] != 'Chefe':
                    pas = terminal.pop(1)
                    aviao.append(pas)
                    menu()

                else:
                    pas = terminal.pop(0)
                    aviao.append(pas)
                    menu()
    except IndexError:
        print('Todos estão no avião.')
    
mostrar(terminal,aviao)
txt_aviao(aviao)