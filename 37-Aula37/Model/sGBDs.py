from Model.squads import Squads
from Model.linguagemBackEnd import LinguagemBackEnd
from Model.frameworkFrontEnd import FrameworkFrontEnd

class SGBDs: 
    def __init__(self):
        self.id_SGBDs = 0
        self.SGBDs = ''
        self.SGBDs_desc = ''

    def __str__(self):
        return f'{self.id_SGBDs};{self.SGBDs};{self.SGBDs_desc}'