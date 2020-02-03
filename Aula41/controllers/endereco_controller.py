from flask_restful import Resource
from  flask import  request

from Aula41.model.endereco_model import EnderecoModel
from  Aula41.dao.endereco_dao import EnderecoDao

class EnderecoController (Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        logradouro = request.json['logradouro']
        numero = request.json['numero']
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = request.json['cep']
        endereco = EnderecoModel(logradouro, numero, complemento, bairro, cidade, cep)
        return self.dao.insert(endereco)

    def put(self, id):
        logradouro = request.json['logradouro']
        numero = request.json['numero']
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = request.json['cep']
        endereco = EnderecoModel(logradouro, numero, complemento, bairro, cidade, cep, id)
        return self.dao.update(endereco)

    def delete(self, id):
         return self.dao.remove(id)