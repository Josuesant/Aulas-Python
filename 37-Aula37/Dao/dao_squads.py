import MySQLdb
from Model.squads import Squads

#---- Criação da classe Squads_dao
class Squads_dao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans14', user='padawans14', passwd='jm2019')
    cursor = conexao.cursor()

    #---- Função para Inserir/Criar  
    def Create (self, squads:Squads):
        comando = f""" INSERT INTO tb_squads
        (
        id_time
        ,nome_time
        ,descricao
        ,Numero_pessoas
        ,id_LinguagemBackEnd
        ,id_FrameworkFrontEnd
        ,id_SGBDs
        )
        VALUES
        (

            {squads.id_time},
            '{squads.nome_time}',
            '{squads.descricao}',
            {squads.Numero_pessoas},
            {squads.id_LinguagemBackEnd},
            {squads.id_FrameworkFrontEnd},
            {squads.id_SGBDs}

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    #---- Função para Ler/Listar  
    def Read (self):
        comando = f"SELECT * FROM tb_squads AS P LEFT JOIN tb_LinguagemBackEnd AS E ON P.id_LinguagemBackEnd = E.ID"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    #---- Função para Ler/Listar por id
    def Read_id(self, id):
        comando = f"SELECT * FROM tb_squads AS P LEFT JOIN tb_LinguagemBackEnd AS E ON P.ENDERECO_ID = E.ID WHERE P.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado    

    #---- Função para Alterar
    def Update (self, squads:Squads):
        comando = f""" UPDATE tb_squads
        SET
            id_time = '{squads.id_time}',
            nome_time ='{squads.nome_time}',
            Numero_pessoas = {squads.Numero_pessoas},
            id_LinguagemBackEnd = {squads.id_LinguagemBackEnd.id},
            id_FrameworkFrontEnd = {squads.id_FrameworkFrontEnd.id},
            id_SGBDs = {squads.id_SGBDs.id},
        WHERE ID = {squads.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    #---- Função para Deletar 
    def Delete (self, id):
        comando = f"DELETE FROM tb_squads WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()