import sys
sys.path.append('C:/Users/900172/Documents/JosueHBSIS/GitHub/Aulas-Python/34-Aula34')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)