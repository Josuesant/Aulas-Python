from Dao.dao_sGBDs import SGBDs_dao
from Model.sGBDs import SGBDs

class Controller_sgbds (): 
    dao = SGBDs_dao()

    def Creater (self, sgbds: SGBDs):
        self.dao.Create(sgbds)

    def Read (self):  
        tupla = self.dao.Read
        sgbds = SGBDs(tupla[0], tupla[1], tupla[2])
        return sgbds

    def Read_id(self, id):
        tupla = self.dao.Read_id(id)
        squads = SGBDs(tupla[0], tupla[1], tupla[2])
        return sgbds

    def Update (self, sgbds: SGBDs):
        self.dao.Update (sgbds) 

    def Delete (self, id):
        self.dao.Delete(id)     