from Dao.dao_linguagemBackEnd import LinguagemBackEnd_dao
from Model.linguagemBackEnd import LinguagemBackEnd

class Controller_linguagemBackEnd (): 
    dao = LinguagemBackEnd_dao

    def Creater (self backend: LinguagemBackEnd):
        return self.dao.Create(backend)

    def Read (self):  
        tupla = self.dao.Read
        backend = LinguagemBackEnd(tupla[0], tupla[1], tupla[2])
        return backend

    def Read_id(self, id):
        tupla = self.dao.Read_id(id)
        backend = LinguagemBackEnd(tupla[0], tupla[1], tupla[2])
        return backend   

    def Update (self, backend: LinguagemBackEnd):
        self.dao.Update (backend) 

    def Delete (self, id):
        self.dao.Delete(id) 