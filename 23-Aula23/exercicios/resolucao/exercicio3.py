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


class Cadastro:
    def __init__(self):
        self.lista=[]
        self.ler() # ler o arquivo e criar a lista com dicionario dos clientes. 

    def ler(self):
        try:

            arquivo = open('23-Aula23/exercicios/resolucao/cadastro2.txt','r')
            for pessoa in arquivo:
                pessoa = pessoa.strip().split(';')
                # 1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117
                dic = {'codigo':pessoa[0],'nome':pessoa[1],'idade':pessoa[2],
                    'sexo':pessoa[3],'email':pessoa[4],'telefone':pessoa[5]}
                self.lista.append(dic)

        finally: #garante que o arquivo será fechado no final!!!!!
            arquivo.close()

    def salvar(self,nome,atributo='a'):
        try:
            arquivo = open(f'23-Aula23/exercicios/resolucao/{nome}.txt',atributo)
            for pessoa in self.lista:
                texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['idade']};{pessoa['sexo']};{pessoa['email']};{pessoa['telefone']}\n"
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

        codigo = str ( int(self.lista[-1]['codigo']) + 1 )

        dic = {'codigo':codigo,'nome':nome,'idade':idade,
               'sexo':sexo,'email':email,'telefone':telefone}
        self.lista.append(dic)

    def consulta(self,codigo):
        for pessoa in self.lista:
            if int(pessoa['codigo']) == codigo:
                print(f'''
Codigo: {pessoa['codigo']}
Nome: {pessoa['nome']}
Idade: {pessoa['idade']}
Sexo: {pessoa['sexo']}
Email: {pessoa['email']}
Telefone: {pessoa['telefone']}
                       ''')
                break

# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!
    def atualizar(self,codigo):
         for pessoa in self.lista:
            if int(pessoa['codigo']) == codigo:
                nome = input('Digite o nome do cliente: ')
                idade = input('Digite a idade: ')
                sexo = input('Digite sexo: ')
                email = input('Digite o email: ')
                telefone = input('Digite o telefone: ')
                ### atualizar dados:
                pessoa['nome'] = nome
                pessoa['idade'] = idade
                pessoa['sexo'] = sexo
                pessoa['email'] = email
                pessoa['telefone'] = telefone

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