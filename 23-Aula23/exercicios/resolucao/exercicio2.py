# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)



# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um 
# arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem 
# o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.


dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

class Cliente:
    def __init__ (self,dadobruto):
        self.dado_bruto = dadobruto
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None

    def tratamento(self):
        dados = self.dado_bruto
        dados = dados.strip()
        dados = dados.split(';')
        self.codigo = int(dados[0])
        self.nome = dados[1]
        self.idade = int(dados[2])
        self.sexo = dados[3]
        self.email = dados[4]
        self.telefone = dados[5]

    def salvar(self,nome,atributo='a'):
        arquivo = open(f'23-Aula23/exercicios/resolucao/{nome}.txt',atributo)
        #texto = 
        texto = f'{self.dado_bruto}\n'
        arquivo.write(texto)
        arquivo.close()

    #ou....
    # def salvar(self,nome,atributo):
    #     if atributo == 'a':
    #         arquivo = open(f'23-Aula23/exercicios/resolucao/{nome}.txt',atributo)
    #         #texto = 
    #         texto = f'{self.dado_bruto}\n'
    #         arquivo.write(texto)
    #         arquivo.close()
    #     elif atributo == 'r':
    #         ''' perde o sentido do nome salvar.... mas como exemplo vale :-)
    #         '''
    #         arquivo = open(f'23-Aula23/exercicios/resolucao/{nome}.txt',atributo)
    #         for dados in arquivo:
    #             dados = dados.strip().split(';')
    #             self.codigo = int(dados[0])
    #             self.nome = dados[1]
    #             self.idade = int(dados[2])
    #             self.sexo = dados[3]
    #             self.email = dados[4]
    #             self.telefone = dados[5]
    #         arquivo.close()
    #     elif atributo == 'w':
    #         arquivo = open(f'23-Aula23/exercicios/resolucao/{nome}.txt',atributo)
    #         #texto = 
    #         texto = f'{self.dado_bruto}\n'
    #         arquivo.write(texto)
    #         arquivo.close()


    
    def atualizar(self):
        # self.codigo = int(input('Digi')) CODIGO NÃO!
        self.nome = input('Digite o novo nome do cliente: ')
        self.idade = int(input('Digite a nova idade do cliente: '))
        self.sexo = input('Digite o sexo do cliente: ')
        self.email = input('digite o email do cliente: ')
        self.telefone = input('Digite o telefone: ')       
        self.dado_bruto = f'{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}'
        self.salvar("arquivo_novo",'w')

pessoa = Cliente(dadobruto)

pessoa.tratamento()
pessoa.salvar('salvarcliente')

print(f'Codigo: {pessoa.codigo}')
print(f'Nome: {pessoa.nome}')
print(f'Idade: {pessoa.idade}')
print(f'Sexo: {pessoa.sexo}')
print(f'Email: {pessoa.email}')
print(f'Telefone: {pessoa.telefone}')

pessoa.atualizar()

print(f'Codigo: {pessoa.codigo}')
print(f'Nome: {pessoa.nome}')
print(f'Idade: {pessoa.idade}')
print(f'Sexo: {pessoa.sexo}')
print(f'Email: {pessoa.email}')
print(f'Telefone: {pessoa.telefone}')