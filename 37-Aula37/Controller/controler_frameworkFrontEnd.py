from Dao.dao_frameworkFrontEnd import FrameworkFrontEnd_dao
from Model.frameworkFrontEnd import FrameworkFrontEnd


class Controller_frameworkFrontEnd ():
    dao = FrameworkFrontEnd_dao

    def Creater (self, frontend:FrameworkFrontEnd):
        return self.dao.Create(frontend)

    def Read (self):  
        tupla = self.dao.Read
        frontend = FrameworkFrontEnd(tupla[0], tupla[1], tupla[2])
        return frontend

    def Read_id(self, id):
        tupla = self.dao.Read_id(id)
        frontend = FrameworkFrontEnd(tupla[0], tupla[1], tupla[2])
        return frontend

    def Update (self, frontend:FrameworkFrontEnd):
        self.dao.Update (frontend) 

    def Delete (self, id):
        self.dao.Delete(id) 