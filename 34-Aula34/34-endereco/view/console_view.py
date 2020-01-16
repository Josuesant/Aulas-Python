import sys
sys.path.append('C:/Users/900172/Documents/JosueHBSIS/GitHub/Aulas-Python/34-Aula34/34-endereco')
from controller.endereco_controller import EnderecoController

ec = EnderecoController()

for e in ec.listar_todos():
    print(e)