
class Squads:
    def __init__(self, nome_time, descricao, Numero_pessoas):
        self.id_time = 0
        self.nome_time = nome_time
        self.descricao = descricao
        self.Numero_pessoas = Numero_pessoas
        self.id_LinguagemBackEnd = 'NULL'
        self.id_FrameworkFrontEnd = 'NULL'
        self.id_SGBDs = 'NULL'

    def __str__(self):
        return f'{self.id_time};{self.nome_time};{self.Numero_pessoas};{self.id_LinguagemBackEnd};{self.id_FrameworkFrontEnd};{self.id_SGBDs}'




