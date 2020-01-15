import MySQLdb
class Db:
    def __init__(self):
        self.conexao = MySQLdb.connect(host='localhost', database='auladb', user='root', passwd='')
        self.cursor = self.conexao.cursor()

    def menu (self):
        while True:
            op = int(input('\nEscolha uma oopção: \n 1 - Exibir \n 2 - Buscar por ID \n 3 - Buscar por Sobrenome \n 4 - Salvar \n 5 - Alterar \n 6 - Deletar \n 7 - Sair \n Opção desejada: '))
            if op == 1:
                self.__listar_todos()

            elif op == 2:
                self.id = input('Qual ID você quer pesquisar? ')
                self.__buscar_por_id(id)

            elif op == 3:
                self.sobrenome = input('Qual Sobrenome você quer pesquisar? ')
                self.__buscar_por_sobrenome(self.cursor, self.sobrenome)

            elif op == 4:
                self.__dados()
                self.__salvar(cn, cr, nome, sobrenome, idade)  

            elif op == 5:
                self.__dados()
                self.__alterar(self.__dados)
                
            elif op == 6:
                self.id = input('Qual ID você quer Deletar? ')
                self.__deletar()

            elif op == 7:
                break

            else:
                print('\nOpção Inválida! Digite um número de 1 a 7\n')

    def __dados (self):
        self.NOME = input('Qual o nome? ')
        self.SOBRENOME = input('Qual sobrenome? ')
        self.IDADE = input('Qual idade? ')

    def __listar_todos(self):
        self.cursor.execute ('SELECT * FROM pessoa AS p JOIN endereco AS e ON p.ENDERECO = e.Id')
        pessoas = self.cursor.fetchall()

        for p in pessoas:
            print('-'*50)
            print(p)
            print('-'*50)   

        #buscar pessoas por id
    def __buscar_por_id (self, id):
        self.cursor.execute(f'SELECT * FROM pessoa WHERE id = {self.id}')
        self.pessoa = self.cursor.fetchone()
        for p in self.pessoa:
            print(p)            

        #buscar pessoas por sobrenome
    def __buscar_por_sobrenome(self, cursor, sobrenome):
        self.cursor.execute(f"SELECT * FROM pessoa WHERE SOBRENOME like '{self.sobrenome}%' ")
        for p  in  self.cursor.fetchall():
            print(p)

    #salvar pessoa
    def __salvar(self, cn, cr, nome, sobrenome, idade, endereco_id='NULL'):
        self.cr.execute(f"INSERT INTO pessoa (NOME, SOBRENOME, IDADE, ENDERECO_ID )VALUES('{self.nome}', '{self.sobrenome}','{self.idade}',{self.endereco_id})")
        self.cn.commit()

    #alterar pessoa
    def __alterar(self, cn, cr, id, nome, sobrenome, idade, endereco_id='NULL'):
        self.cr.execute(f"UPDATE pessoa SET NOME='{self.nome}', SOBRENOME='{self.sobrenome}', IDADE='{self.idade}', ENDERECO_ID={self.endereco_id} WHERE ID={id} ")
        self.cn.commit()

    #deletar pessoa por ID
    def __deletar(self, cn, cr, id):
        self.cr.execute(f'DELETE FROM pessoa WHERE ID={id}')
        self.cn.commit()


db = Db()
db.menu()