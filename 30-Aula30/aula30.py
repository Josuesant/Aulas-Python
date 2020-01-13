#--- Banco de Dados
#--- SGBD _ Sistema Gerenciador de Banco de Dados
#--- MySQL, SqlServer ...

#--- Mysql = MariaDb

# CRUD 
# C = CREATE  INSERIR/SALVAR - 
# R = READ 
# U = UPTADE 
# D = DELETE

from flask_mysqldb import MySQLdb 
from contextlib import closing

__dados = {
        'host':'mysql.topskills.study',
        'database': 'topskills01',
        'user': 'topskills01',
        'passwd': 'ts2019',
        'port':3306}

def cadastrar (NOME, IDADE):
    with closing(MySQLdb.connect(**__dados)) as conn: 
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO topskills01.King_Of_list (NOME, SOBRENOME, SKILLS, ADM_WHATS, IDADE) VALEUS ('{Gustavo}', '{Votolini}', '{Explosivo}', {0}, {17}) ") 
        conn.commit()

def consultarALL ():
    with closing(MySQLdb.connect(**__dados)) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM topskills01.King_Of_list') 
        print('\n Só uma linha: ', cursor.fetchone())
        print('\n Várias linhas: ', cursor.fetchall())

op = 's'
while op == 's':
    NomePessoa = input('Digite um nome de alguém: ')
    Sobrenome = input('Digite um sobrenome: ')
    Idade = int(input('Digite uma idade: '))
    cadastrar(NOME, IDADE)
    op = input('\nDeseja cadastrar mais alguém? (S/N) ')

cadastrar(NOME,IDADE)                         
