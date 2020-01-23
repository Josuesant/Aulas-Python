from Model.squads import Squads
from Model.linguagemBackEnd import LinguagemBackEnd
from Model.sGBDs import SGBDs

class FrameworkFrontEnd:
    def __init__(self):
        self.id_FrontEnd = 0
        self.FrameworkFrontEnd = ''
        self.FrontEnd_desc = ''

    def __str__(self):
        return f'{self.id_FrontEnd};{self.FrameworkFrontEnd};{self.FrontEnd_desc}' 