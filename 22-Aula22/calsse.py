class Pessoa:
    '''
    Esta classe é uma demostração para aula
    '''
    def __init__(self, nome1, idade1, telefone1, sexo1):
        ''' O __init__ é o motor que irá iniciar as variáveis da classe
            O self é o que irá conecta toda classe
        '''

        # Atributos ######
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.sexo = sexo1
        #
        self.divida = None
        self.cansada = 'nao'
        self.viva = True
        self.fome = 'sim'
        self.sede = 'tambem'

    def respira(self, respirar):
        if self.viva == True:
            if respirar == True:
                self.viva = True    

    def dorme(self):

    def carre(self):

    def bebe(self):

    def come(self):

    def multiplica(self):                        