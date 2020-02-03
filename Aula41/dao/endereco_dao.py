import MySQLdb

from Aula41.model.endereco_model import EnderecoModel

class EnderecoDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM 01_MDG_ENDERECO")
        enderecos = self.cursor.fetchall()
        lista_enderecos = []
        for e in enderecos:
            enderecos = EnderecoModel(e[1], e[2], e[3], e[4], e[5], e[6], e[0])
            lista_enderecos.append(enderecos.__dict__)
        return lista_enderecos

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM 01_MDG_ENDERECO WHERE ID = {}".format(id))
        endereco = self.cursor.fetchone()
        e = EnderecoModel(e[1], e[2], e[3], e[4], e[5], e[6], e[0])
        return e.__dict__

    def insert(self, endereco : EnderecoModel):
        self.cursor.execute("""
                    INSERT INTO 01_MDG_ENDERECO 
                    (LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, CIDADE, CEP) 
                    VALUES('{}','{}','{}','{}','{}','{}')""".format(endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.cep))
        self.connection.commit()
        id = self.cursor.lastrowid
        endereco.id = id
        return endereco.__dict__

    def update(self, endereco : EnderecoModel):
        self.cursor.execute("""
                    UPDATE 01_MDG_ENDERECO 
                        SET 
                            LOGRADOURO = '{}',
                            NUMERO = '{}',
                            COMPLEMENTO = '{}',
                            BAIRRO = '{}',
                            CIDADE = '{}',
                            CEP = '{}'
                        WHERE ID = {}
                 """.format(endereco.logradouro, endereco.numero, endereco.complemento, endereco.bairro, endereco.cidade, endereco.cep, endereco.id))
        self.connection.commit()
        return endereco.__dict__

    def remove(self, id):
        self.cursor.execute("DELETE FROM 01_MDG_ENDERECO WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido o endereco de id : {}'.format(id)
