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


controller = Controller_squads()

frame = FrameworkFrontEnd ('Visual Studio', 'IDE Certificada')

ling = LinguagemBackEnd ('c#', 'alto nível')

sgb = SGBDs ('oracle', 'pesquisas')

equipe = Squads ('Grupo Alpha', 'Benchmarking de mercado', 7)

print (controller.Creater(equipe))