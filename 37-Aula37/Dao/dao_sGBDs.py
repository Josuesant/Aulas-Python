import MySQLdb
from Model.sGBDs import SGBDs

#---- Criação da classe SGBDs_dao
class SGBDs_dao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans14', user='padawans14', passwd='jm2019')
    cursor = conexao.cursor()

    #---- Função para Inserir/Criar  
    def Create (self):
        comando = f""" INSERT INTO tb_SGBDs
        (
        id_SGBDs
        ,SGBDs
        ,SGBDs_desc
        )
        VALUES
        (
            {sGBDs.id_SGBDs},
            '{sGBDs.SGBDs}',
            '{sGBDs.SGBDs_desc}'

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    #---- Função para Ler/Listar  
    def Read (self):
        comando = f"SELECT * FROM tb_SGBDs"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    #---- Função para Ler/Listar por id
    def Read_id(self, id):
        comando = f"SELECT * FROM tb_SGBDs WHERE P.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado    

    #---- Função para Alterar
    def Update (self, sGBDs: SGBDs):
        comando = f""" UPDATE tb_SGBDs
        SET
            id_SGBDs = {sGBDs.id_SGBDs},
            SGBDs ='{sGBDs.SGBDs}',
            SGBDs_desc = {sGBDs.SGBDs_desc},
        WHERE ID = {sGBDs.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    #---- Função para Deletar 
    def Delete (self, id):
        comando = f"DELETE FROM tb_SGBDs WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()