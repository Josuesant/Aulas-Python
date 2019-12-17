# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto. ok
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None

# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)

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


pessoa = Cliente(dadobruto)

pessoa.tratamento()

print(f'Codigo: {pessoa.codigo}')
print(f'Nome: {pessoa.nome}')
print(f'Idade: {pessoa.idade}')
print(f'Sexo: {pessoa.sexo}')
print(f'Email: {pessoa.email}')
print(f'Telefone: {pessoa.telefone}')