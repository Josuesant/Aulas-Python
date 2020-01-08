embarque = ['Presidiário','Policial' , 'Piloto', 'Oficial1', 'Oficial2', 'Chefe', 'Comissária1','Comissária2']

def txt_terminal ():
    dados = ','.join(embarque) # Convertendo uma lista em String e atribuindo ela a variável dados
    arquivo = open('29-Aula29/lista_terminal.txt', 'w') # Criando arquivo
    arquivo.writelines(dados)  # Inserindo conteúdo no arquivo
    arquivo.close() # Fehando arquivo
    dados = dados.split(',') # Convertendo a String em uma lista / Não precisaria, era só colocar no return a lista embarque
    return dados

def txt_aviao (aviao):
    dados = ','.join(aviao)       
    arquivo = open('29-Aula29/lista_aviao.txt', 'w') # Criando arquivo
    arquivo.writelines(dados)  # Inserindo conteúdo no arquivo
    arquivo.close() # Fehando arquivo    
