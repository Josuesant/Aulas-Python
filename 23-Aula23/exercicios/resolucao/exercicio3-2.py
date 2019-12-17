# Aula 22 - 10-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)



# 1) Crie uma classe cadastro.
# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.
# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
# 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!

# E se fosse com classe no ligar da lista com dicionario.......


class Cliente:
    def __init__ (self,dadobruto):
        self.dado_bruto = dadobruto
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None
        self.tratamento()

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
    
    def atualizar(self):
        # self.codigo = int(input('Digi')) CODIGO NÃO!
        self.nome = input('Digite o novo nome do cliente: ')
        self.idade = int(input('Digite a nova idade do cliente: '))
        self.sexo = input('Digite o sexo do cliente: ')
        self.email = input('digite o email do cliente: ')
        self.telefone = input('Digite o telefone: ')       
        self.dado_bruto = f'{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}'
        #-
    def __eq__ (self,valor):
        ''' habilitar a operação =='''
        return self.codigo == valor

    def __str__(self):
        ''' habilita para printar os dados do cliente'''
        texto = f'''
Codigo: {self.codigo}
Nome: {self.nome}
Idade: {self.idade}
Sexo: {self.sexo}
Email: {self.email}
Telefone: {self.telefone}
                '''
        return texto



class Cadastro:
    def __init__(self):
        self.lista=[]
        self.ler() # ler o arquivo e criar a lista com dicionario dos clientes. 

    def ler(self):
        try:

            arquivo = open('23-Aula23/exercicios/resolucao/cadastro2.txt','r')
            for dado_bruto in arquivo:
                dado_bruto = dado_bruto.strip() #retirar o \n
                self.lista.append(Cliente(dado_bruto))

        finally: #garante que o arquivo será fechado no final!!!!!
            arquivo.close()

    def salvar(self,nome,atributo='a'):
        try:
            arquivo = open(f'23-Aula23/exercicios/resolucao/{nome}.txt',atributo)
            for pessoa in self.lista:
                texto = f'{pessoa.dado_bruto}\n'
                arquivo.write(texto)
        finally:
            arquivo.close()

    def cadastrar(self):
        ###  codigo = Já retornamos!!!
        nome = input('Digite o nome do cliente: ')
        idade = input('Digite a idade: ')
        sexo = input('Digite sexo: ')
        email = input('Digite o email: ')
        telefone = input('Digite o telefone: ')

        codigo = int(self.lista[-1].codigo + 1)

        texto = f'{codigo};{nome};{idade};{sexo};{email};{telefone}'
        self.lista.append(Cliente(texto))

    def consulta(self,codigo):
        for pessoa in self.lista:
            if pessoa == codigo:
                print(pessoa)
                break

    def atualizar(self,codigo):
         for pessoa in self.lista:
            if pessoa == codigo:
                
                pessoa.atualizar()

                # Salvar no arquivo......

                self.salvar('cadastro_atualizado','w')

                break # para finalizar a pesquisa!




p = Cadastro()
# p.cadastrar()
# p.salvar()

p.consulta(20)

p.atualizar(20)

p.consulta(20)


# for i in range (20):
#     print(p.lista[i])