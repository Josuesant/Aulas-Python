import MySQLdb 
from Model.frameworkFrontEnd import FrameworkFrontEnd

#---- Criação da classe FrameworkFrontEnd_dao
class FrameworkFrontEnd_dao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans14', user='padawans14', passwd='jm2019')
    cursor = conexao.cursor()

    #---- Função para Inserir/Criar  
    def Create (self):
        comando = f""" INSERT INTO tb_FrameworkFrontEnd
        (
        id_FrontEnd
        ,FrameworkFrontEnd
        ,FrontEnd_desc
        )
        VALUES
        (
            {frameworkFrontEnd.id_FrontEnd},
            '{frameworkFrontEnd.FrameworkFrontEnd}',
            '{frameworkFrontEnd.FrontEnd_desc}'

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    #---- Função para Ler/Listar  
    def Read (self):
        comando = f"SELECT * FROM tb_FrameworkFrontEnd"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    #---- Função para Ler/Listar por id
    def Read_id(self, id):
        comando = f"SELECT * FROM tb_FrameworkFrontEnd WHERE P.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado    

    #---- Função para Alterar
    def Update (self, frameworkFrontEnd: FrameworkFrontEnd):
        comando = f""" UPDATE tb_FrameworkFrontEnd
        SET
            id_FrontEnd = {frameworkFrontEnd.id_FrontEnd},
            FrameworkFrontEnd ='{frameworkFrontEnd.FrameworkFrontEnd}',
            FrontEnd_desc = '{frameworkFrontEnd.FrontEnd_desc}',
        WHERE ID = {frameworkFrontEnd.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    #---- Função para Deletar 
    def Delete (self, id):
        comando = f"DELETE FROM tb_FrameworkFrontEnd WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()