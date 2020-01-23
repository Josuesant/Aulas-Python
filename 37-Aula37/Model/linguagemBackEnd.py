from Model.squads import Squads
from Model.frameworkFrontEnd import FrameworkFrontEnd
from Model.sGBDs import SGBDs

class LinguagemBackEnd:
    def __init__(self):
        self.id_BackEnd = 0
        self.LinguagemBackEnd = ''
        self.BackEnd_desc = ''

    def __str__(self):
        return f'{self.id_BackEnd};{self.LinguagemBackEnd};{self.BackEnd_desc}' 