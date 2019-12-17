# Aula 19 - 04-12-2019
# Lista com for e metodos

# Como comer um gigante.... é com um pedaço de cada vez.
# Na hora de fazer este exercicio, atentar para 

# Com o arquivo de cadastro.txt onde possui os seguintes dados: codigo cliente, nome, idade, sexo, e-mail e telefone
# 1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.
# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.
# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing


#1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes

def ler_dados():
    cabecalho = ['codigo_cliente', 'nome', 'idade', 'sexo', 'email', 'telefone']
    arquivo = open('19-Aula19/exercicios/Resolução/cadastro.txt','r')
    lista = []
    for nome in arquivo:
        dic = {}
        nome = nome.strip()
        nome = nome.split(';')

        for i in range( len(cabecalho) ):
            dic[ cabecalho[i] ] = nome[i]

        lista.append(dic)

    arquivo.close()
    
    return lista


#2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.

def salvar(lista,nome):
    arquivo = open(f'19-Aula19/exercicios/Resolução/{nome}.txt','a')
  
    for pessoa in lista:
        texto = f"{pessoa['codigo_cliente']};{pessoa['nome']};{pessoa['idade']};{pessoa['sexo']};{pessoa['email']};{pessoa['telefone']}\n"
        arquivo.write(texto)
    arquivo.close()




######################################################################################
# Outro modos
######################################################################################
# def salvar(lista,nome):
#     arquivo = open(f'19-Aula19/exercicios/Resolução/{nome}.txt','a')
#     cabecalho = ['codigo_cliente', 'nome', 'idade', 'sexo', 'email', 'telefone']
#     for pessoa in lista:
#         cont = 0
#         for chave in cabecalho:
#             if cont == 0:
#                 texto = f'{pessoa[chave]}'
#                 cont += 1
#             else:
#                 texto = texto+f';{pessoa[chave]}'
#         arquivo.write(texto+'\n')
#     arquivo.close()


# def salvar(lista,nome):
#     arquivo = open(f'19-Aula19/exercicios/Resolução/{nome}.txt','a')
#     cabecalho = list(lista[0].keys()) # Estou retirando a chave dos dicionários
#     #cabecalho = list(lista[0]) # outra forma de retirar a chave dos dicionários 
#     ##### Tem que adicionar o cabeçalho ao arquivo #######
#     texto = ';'.join(cabecalho) # Transforma a lista para uma string seria o contrario do .splint()
#     arquivo.write(texto+'\n')
#     for pessoa in lista:
#         cont = 0
#         for chave in cabecalho:
#             if cont == 0:
#                 texto = f'{pessoa[chave]}'
#                 cont += 1
#             else:
#                 texto = texto+f';{pessoa[chave]}'
#         arquivo.write(texto+'\n')
#     arquivo.close()

################


def maioridade(lista):
    maior = []
    menor = []
    for pessoa in lista:
        if int(pessoa['idade']) >= 18:
            maior.append(pessoa)
        else:
            menor.append(pessoa)
    salvar(maior,'maior')
    salvar(menor,'menor')
    return maior

# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.


def conte_hm(lista):
    mulher = []
    homem = []
    for pessoa in lista:
        if pessoa['sexo'] == 'f':
            mulher.append(pessoa)
        else:
            homem.append(pessoa)
    print(f'A quantidade de homens é {len(homem)}')
    print(f'A quantidade de mulheres é {len(mulher)}')
    salvar(mulher,'mulher')
    salvar(homem,'homem')

######################################################################################
# Outro modos
######################################################################################

# def conte_hm(lista):
#     mulher = []
#     cont_m = 0
#     homem = []
#     cont_h = 0
#     for pessoa in lista:
#         if pessoa['sexo'] == 'f':
#             mulher.append(pessoa)
#             cont_m += 1
#         else:
#             homem.append(pessoa)
#             cont_h += 1
#     print(f'A quantidade de homens é {cont_h}')
#     print(f'A quantidade de mulheres é {cont_m}')
#     salvar(mulher,'mulher')
#     salvar(homem,'homem')



# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing


def consulta(lista,codigo):
    for pessoa in lista:
        if int(pessoa['codigo_cliente'])==codigo:
            if pessoa['sexo'] == 'f':
                if int(pessoa['idade']) <= 16: #
                    dados(pessoa)
                    print(f"Ola {pessoa['nome']}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!")
                    break # O break é importante para poder parar a pesquisa quando o item for achado
                elif int(pessoa['idade']) > 16 and int(pessoa['idade']) <= 18 :
                    dados(pessoa)
                    print(f"Olá {pessoa['nome']}! Quer experimentar nosso refigerante sabor alegria! O seu cruch vai adorar!")
                    break
                else:
                    dados(pessoa)
                    print(f"Olá {pessoa['nome']}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico com o dobro de sabor!!!")
                    break
            else:
                if int(pessoa['idade']) <= 16:
                    dados(pessoa)
                    print(f"Ola {pessoa['nome']}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!")
                    break
                elif int(pessoa['idade']) > 16 and int(pessoa['idade']) <= 18 :
                    dados(pessoa)
                    print(f"Olá {pessoa['nome']}! Quer experimentar nosso refigerante sabor Corriga de carros! A sua amada vai adorar!")
                    break
                else:
                    dados(pessoa)
                    print(f"Olá {pessoa['nome']}! Já experimentou nossa cerveja? alto teor alcoolico com o dobro do amargor!!!")
                    break
    print('\n')



def dados(dicionario):
    texto=f'''
Código cliente: {dicionario['codigo_cliente']}
Nome: {dicionario['nome']}
Idade: {dicionario['idade']}
Sexo: {dicionario['sexo']}
Email: {dicionario['email']} 
Telefone: {dicionario['telefone']}\n'''
    print(texto)
       




lista1 = ler_dados()
maioridade(lista1)
conte_hm(lista1)

sair = 'n'
while not sair == 's':
    codigo = int(input('Digite o número: '))
    consulta(lista1,codigo)
    sair = input('Digite s para sair: ')


































































































































































































































# # ovo de pascua:

# interar dicionários:

# lista1=[
# {'codigo_cliente': '477', 'nome': 'Gianfranco', 'idade': '47', 'sexo': 'm', 'email': 'programadorardamax@hotmail.com', 'telefone': '035955256942'},
# {'codigo_cliente': '478', 'nome': 'Giancarlo', 'idade': '25', 'sexo': 'f', 'email': 'flavinha-rebels01@bol.com.br', 'telefone': '048956214192'},
# {'codigo_cliente': '479', 'nome': 'Cleber', 'idade': '16', 'sexo': 'm', 'email': 'renan_godoy13@hotmail.com', 'telefone': '025905277376'},
# {'codigo_cliente': '480', 'nome': 'Maximiliano', 'idade': '35', 'sexo': 'f', 'email': 'bibica-banho@bol.com.br', 'telefone': '027903466043'}
# ]

# for i in lista1[0]:
#     print(i)
# 'codigo_cliente' # imprime a chave do dicionário
# 'nome'
# 'idade'
# 'sexo'
# 'email'
# 'telefone'


# for i in lista1[0]:
#     print(f'{i}= {lista1[0][i]}')
# 'codigo_cliente= 477' # imprime a chave e o valor
# 'nome= Gianfranco'
# 'idade= 47'
# 'sexo= m'
# 'email= programadorardamax@hotmail.com'
# 'telefone= 035955256942'


# for i,j in lista1[0].itens():
#     print(f'{i}= {j}')
# 'codigo_cliente= 477' # imprime a chave e o valor
# 'nome= Gianfranco'
# 'idade= 47'
# 'sexo= m'
# 'email= programadorardamax@hotmail.com'
# 'telefone= 035955256942'

# Converter 2 lista em um dicionário

# chaves = ['codigo_cliente','nome','idade','sexo','email','telefone']

# valores = ['477','Gianfranco','47','m','programadorardamax@hotmail.com','035955256942']

# dicionario = dict(zip(chave,valores))
# {'codigo_cliente': '477', 'nome': 'Gianfranco', 'idade': '47', 'sexo': 'm', 'email': 'programadorardamax@hotmail.com', 'telefone': '035955256942'}

# Transformando uma dicionário em uma lista de tuplas

# lista = list(a.items())
# [('codigo_cliente', '477'), ('nome', 'Gianfranco'), ('idade', '47'), ('sexo', 'm'), ('email', 'programadorardamax@hotmail.com'), ('telefone', '035955256942')]

# Transformando uma lista de tuplas em um dicionário.

# dicionario = dict(lista)
# {'codigo_cliente': '477', 'nome': 'Gianfranco', 'idade': '47', 'sexo': 'm', 'email': 'programadorardamax@hotmail.com', 'telefone': '035955256942'}



