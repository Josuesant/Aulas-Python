# Crie uma classe cliente 
# 1) Ela deve ter como atributos: codigo, cpf, nome, idade, sexo
# 2) Como metodos deve ter: receber salario, compar, pagar divida
# Quando aumenta o dinheiro da carteira.
# Quando compra aumenta os bens e diminui o dinheiro na carteira
# Se comprar e não tiver dinheiro suficiente deve diminuir o dinheiro da carteira e aumenta a divida
# Para pagar a divida tem que  ter dinheiro o suficiente na carteira
# 3) Atributos de estado: dinheiro na carteira, divida, bens


class Cliente: 
    def __init__(self, cod, cpf, nome, idade, sexo):
        self.codigo = cod
        self.cpf = cpf
        self.nome = nome
        self.idade = idade

        self.dinheiro_carteira = 0
        self.divida = 0
        self.bens = []

    def receber_salario (self, dinheiro_carteira ):
        self.dinheiro_carteira +=dinheiro_carteira


    def comprar (self, bens, valor):
        self.bens.append(bens)
        if valor < self.dinheiro_carteira:
            self.dinheiro_carteira -= valor
        else:
            self.divida -= self.dinheiro_carteira - valor
            self.dinheiro_carteira = 0  
            

    def pagar(self, dinheiro_carteira, divida):
            if self.dinheiro_carteira >= self.divida:
                self.divida = 0
            else:
                'Você não tem dinheiro sufuciente para pagar a dívida! '    


cliente = Cliente(1, '128.489.057-31', 'Jose', 25, 'masc')
print(cliente.dinheiro_carteira, cliente.divida)

cliente.receber_salario(2800.00)

cliente.comprar("celular", 1800.00)
              