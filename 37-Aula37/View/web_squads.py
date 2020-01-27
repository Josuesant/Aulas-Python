from flask import Flask, render_template, request, redirect
import sys
sys.path.append('C:/Users/900172/Documents/JosueHBSIS/GitHub/Aulas-Python/37-Aula37')

from Controller.controller_squads import *
from Controller.controller_linguagemBackEnd import *
from Controller.controler_frameworkFrontEnd import *
from Controller.controller_sgbds import *
from Model.squads import Squads
from Model.linguagemBackEnd import LinguagemBackEnd
from Model.frameworkFrontEnd import FrameworkFrontEnd
from Model.sGBDs import SGBDs

app = Flask(__name__)
Squads_controller = Controller_squads()
linguagem_controler = Controller_linguagemBackEnd()
frame_controller = Controller_frameworkFrontEnd()
sgbds_controller = Controller_sgbds()
nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/cadastrar')
def cadastrar():
    squads = Squads()
    squads.id_LinguagemBackEnd = LinguagemBackEnd()
    squads.id_FrameworkFrontEnd = FrameworkFrontEnd()
    squads.id_SGBDs = SGBDs()
    if 'id' in request.args:
        id = request.args['id']
        squads = Squads_controller.Read_id(id)
    return render_template('cadastrar.html', squads = squads)

@app.route('/listar')
def listar():
    squads = Squads_controller.Read()
    return render_template('listar.html', lista = squads)

@app.route('/salvar')
def salvar():
    squads = Squads()
    squads.id_time = request.args['id_time']
    squads.nome_time = request.args['nome_time']
    squads.Numero_pessoas = request.args['Numero_pessoas']
    squads.descricao = request.args['descricao']

    linguagem = LinguagemBackEnd()
    linguagem.id_BackEnd = request.args['id_BackEnd']
    linguagem.LinguagemBackEnd = request.args['LinguagemBackEnd']
    linguagem.BackEnd_desc = request.args['BackEnd_desc']

    framework = FrameworkFrontEnd()
    framework.id_FrontEnd = request.args['id_FrontEnd']
    framework.FrameworkFrontEnd = request.args['FrameworkFrontEnd']
    framework.FrontEnd_desc = request.args['FrontEnd_desc']

    sgbds = SGBDs()
    sgbds.id_SGBDs = request.args['id_SGBDs']
    sgbds.SGBDs = request.args['SGBDs']
    sgbds.SGBDs_desc = request.args['SGBDs_desc']

    squads.linguagem = linguagem
    squads.sgbds = sgbds
    squads.framework = framework

    if pessoa.id == 0:
        equipe_controller.salvar(equipe)
    else:
        equipe_controller.alterar(equipe)
    return redirect('/listar')

@app.route('/excluir')
def excluir():
    id_time = int(request.args['id_equipe'])
    id_BackEnd = request.args['id_linguagem']
    id_FrontEnd = request.args['id_framework']
    id_SGBDs = request.args['id_sgbds']
    Squads_controller.Delete(id)

    if squads != 'None':
        Controller_squads.Delete(id_time)
    return redirect('/listar')

    if id_FrontEnd != 'None':
        Controller_frameworkFrontEnd.Delete(id_FrontEnd)
    return redirect('/listar')

    if id_BackEnd != 'None':
        Controller_linguagemBackEnd.Delete(id_BackEnd)
    return redirect('/listar')

    if id_SGBDs != 'None':
        Controller_sgbds.Delete(id_SGBDs)
    return redirect('/listar')

app.run()