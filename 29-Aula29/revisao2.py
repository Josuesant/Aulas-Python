terminal1 = ['Presidiário','Policial' , 'Piloto', 'Oficial1', 'Oficial2', 'Chefe', 'Comissária1','Comissária2']
aviao = []

def txt_terminal (terminal1):
    terminal = []
    arquivo = open('lista_terminal', 'a') # Criando arquivo
    arquivo = arquivo.readlines()
    arquivo.append(terminal1)   # insira seu conteúdo
    terminal.append(txt_terminal)
    arquivo.close()
    return terminal

txt_terminal(terminal1)