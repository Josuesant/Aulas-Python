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

    def Creater (self):
        return self.dao.Create()

    def Read (self):  
        lista_squads = []
        lista_tuplas = self.dao.squads_todos()
        for p in lista_tuplas:
            squads = squads()
            
            lista_squads.append(squads)
        return lista_squads

    def Read_id(self, id):
        p = self.dao.buscar_por_id(id)
        pessoa = Pessoa()
        pessoa.id =  p[0]
        pessoa.nome = p[1]
        pessoa.sobrenome = p[2]
        pessoa.idade = p[3]
        pessoa.endereco.id = p[5]
        pessoa.endereco.logradouro = p[6]
        pessoa.endereco.numero = p[7]
        pessoa.endereco.complemento = p[8]
        pessoa.endereco.bairro = p[9]
        pessoa.endereco.cidade = p[10]
        pessoa.endereco.cep = p[11]
        return pessoa

    def salvar(self, squads: Squads): 
        squads.id_FrameworkFrontEnd.   

    def Update (self, squads: Squads):
        return 

    def Delete ():
        return              

    
