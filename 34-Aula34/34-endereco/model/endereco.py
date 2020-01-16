class Endereco:
    ID = 0
    LOGRADOURO = ''
    NUMERO = ''
    COMPLEMENTO = ''
    BAIRRO = ''
    CIDADE = ''

    def exportar_txt(self, lista_endereco):
        #----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('34-Aula33/34-endereco/endereco.txt','a') as arquivo:
            #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for e in lista_endereco:
                arquivo.write(f"{str(e)}\n")
    
    def __str__(self):
        return f'{self.ID};{self.LOGRADOURO};{self.NUMERO};{self.COMPLEMENTO};{self.BAIRRO};{self.CIDADE}'