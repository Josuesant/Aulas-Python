from Dao.dao_squads import Squads_dao
from Model.squads import Squads
from Controller.controler_frameworkFrontEnd import Controller_frameworkFrontEnd
from Controller.controller_linguagemBackEnd import Controller_linguagemBackEnd
from Controller.controller_sgbds import Controller_sgbds


class Controller_squads ():
    dao = Squads_dao()
    controler_frameworkFrontEnd = Controller_frameworkFrontEnd()
    controller_linguagemBackEnd = Controller_linguagemBackEnd()
    controller_sgbds = Controller_sgbds

    def Creater (self, squads:Squads):
        self.dao.Create(squads)

    def Read (self):  
        tupla = self.dao.Read
        squads = Squads(tupla[0], tupla[1], tupla[2], tupla[3])
        squads.id_LinguagemBackEnd = tupla[4]
        squads.id_FrameworkFrontEnd = tupla[5]
        squads.id_SGBDs = tupla[6]
        return squads

    def Read_id(self, id):
        tupla = self.dao.Read_id(id)
        squads = Squads(tupla[0], tupla[1], tupla[2])
        squads.id_LinguagemBackEnd = tupla[3]
        squads.id_FrameworkFrontEnd = tupla[5]
        squads.id_SGBDs = tupla[6]
        return squads

    # def salvar(self, squads: Squads): 
    #     salvar = Squads_dao
    #     salvar.Create(squads:Squads)   

    def Update (self, squads: Squads):
        self.dao.Update (squads) 

    def Delete (self, id):
        self.dao.Delete(id)              

    
