from flask import Flask, render_template
import sys
sys.path.append('C:/Users/900172/Documents/JosueHBSIS/GitHub/Aulas-Python/34-Aula34/34-endereco')
from controller.endereco_controller import EnderecoController

app = Flask(__name__)
ec = EnderecoController()

@app.route('/')
def inicio():
    endereco = ec.listar_todos()
    return render_template('index.html', lista = endereco)

app.run()