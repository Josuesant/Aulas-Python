import MySQLdb
class Db:
    def __init__(self):
        self.conexao = MySQLdb.connect(host='localhost', database='auladb', user='root', passwd='')
        self.cursor = self.conexao.cursor()

    def listar_todos(self):
        self.cursor.execute ('SELECT * FROM pessoa AS p JOIN endereco AS e ON p.ENDERECO = e.Id')
        pessoas = self.cursor.fetchall()

        for p in pessoas:
            print('-'*50)
            print(p)
            print('-'*50)   

    def buscar_por_id (self, id):
        self.cursor.execute(f'SELECT * FROM pessoa WHERE id = {1}')
        pessoa = self.cursor.fetchone()
        for p in pessoa:
            print(p)            

db = Db()
db.listar_todos()
db.buscar_por_id(1)        