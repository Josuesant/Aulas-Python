import MySQLdb
from Model.linguagemBackEnd import LinguagemBackEnd

#---- Criação da classe LinguagemBackEnd_dao
class LinguagemBackEnd_dao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans14', user='padawans14', passwd='jm2019')
    cursor = conexao.cursor()

    #---- Função para Inserir/Criar  
    def Create (self):
        comando = f""" INSERT INTO tb_LinguagemBackEnd
        (
        id_BackEnd
        ,LinguagemBackEnd
        ,BackEnd_desc
        )
        VALUES
        (
            {linguagemBackEnd.id_BackEnd},
            '{linguagemBackEnd.LinguagemBackEnd}',
            '{linguagemBackEnd.BackEnd_desc}'

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    #---- Função para Ler/Listar  
    def Read (self):
        comando = f"SELECT * FROM tb_LinguagemBackEnd"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    #---- Função para Ler/Listar por id
    def Read_id(self, id):
        comando = f"SELECT * FROM tb_LinguagemBackEnd WHERE P.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado    

    #---- Função para Alterar
    def Update (self, linguagemBackEnd: LinguagemBackEnd):
        comando = f""" UPDATE tb_LinguagemBackEnd
        SET
            id_BackEnd = {linguagemBackEnd.id_BackEnd},
            LinguagemBackEnd ='{linguagemBackEnd.LinguagemBackEnd}',
            BackEnd_desc = '{linguagemBackEnd.BackEnd_desc}',
        WHERE ID = {linguagemBackEnd.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    #---- Função para Deletar 
    def Delete (self, id):
        comando = f"DELETE FROM tb_LinguagemBackEnd WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()