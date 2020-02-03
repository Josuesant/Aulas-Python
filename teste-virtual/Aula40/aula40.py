from itertools import product

class Distribuicao:

    def __init__(self):
        self.banco_dados = ['MsSqlServer', 'PostgreSQL', 'MongoDb']
        self.backend = ['Python', 'Java', 'PHP']
        self.frontend = ['React', 'Angular', 'Vue']
        self.Mateus = ['Python', 'Angular', 'MongoDb']
        self.Tiago = ['Java', 'Vue', 'PostgreSQL']
        self.Nicole = ['PHP', 'Reagir', 'MsSqlServer']

    def Squads(self):
        banco = self.banco_dados
        backend = self.backend
        frontend = self.frontend
        squads = []

        genComb = product(backend, banco, frontend, repeat=1) # aqui é especificamos o numero de chars que cada combinacao tenha
        for subset in genComb:
            print(subset)
            squads.append(subset)
        print(squads)


distribuicao = Distribuicao()
print(distribuicao.Squads())