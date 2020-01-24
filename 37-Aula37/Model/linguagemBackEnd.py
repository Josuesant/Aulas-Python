
class LinguagemBackEnd:
    def __init__(self, LinguagemBackEnd, BackEnd_desc):
        self.id_BackEnd = 0
        self.LinguagemBackEnd = LinguagemBackEnd
        self.BackEnd_desc = BackEnd_desc

    def __str__(self):
        return f'{self.id_BackEnd};{self.LinguagemBackEnd};{self.BackEnd_desc}' 