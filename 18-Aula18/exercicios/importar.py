# importação da classe. 
from classe2 import FestaHBSIS

# from classe2 import * -É a forma menos indicada para importar uma biblioteca

festa = FestaHBSIS() # Esta atribuindo a variavel festa a classe FestaHBSIS()

festa.ler_cadastro() # É a forma de chamar o metodo da classe.

#festa.consulta(10)

festa.lista_festa()