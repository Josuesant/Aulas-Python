import MySQLdb
# configuração da conexão
conexao = MySQLdb.connect(host='localhost', database='auladb', user='root', passwd='')

#Salvar conexão numa variável
cursor = conexao.cursor()

#Criação de dicionário que representa uma pesoas
dici_pessoa = {'ID': '', 'NOME': '', 'SOBRENOME': '', 'IDADE': 0, 'ENDERECO_ID': 0}


#Criação do comando SQL que é passado para o cursor
comando_sql_select = "SELECT * FROM pessoa"
cursor.execute(comando_sql_select) 

lista_pessoa = []
resultado = cursor.fetchall()
for p in resultado:
    #Criação de dicionário que representa uma pesoas
    dici_pessoa = {'ID': '', 'NOME': '', 'SOBRENOME': '', 'IDADE': 0, 'ENDERECO_ID': 0}
    dici_pessoa['ID'] = p[0]
    dici_pessoa['NOME'] = p[1]
    dici_pessoa['SOBRENOME'] = p[2]
    dici_pessoa['IDADE'] = p[3]
    dici_pessoa['ENDERECO_ID'] = p[4]
    lista_pessoa.append(dici_pessoa)

#Criando arquivo .txt e adicionando os dados e salvando. 
with open ('pessoa.txt', 'a') as arquivo:
    for p in lista_pessoa:
        arquivo.write(f"{p['ID']};{p['NOME']};{p['SOBRENOME']};{p['IDADE']};{p['ENDERECO_ID']}\n")


for p in lista_pessoa:
    print(f'\t{p}')    