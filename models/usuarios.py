from flask_login import UserMixin
from utilidades import *
#from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__="usuarios"
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), primary_key = True)
    endereco = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(15), nullable=False)
    data_cad = db.Column(db.Date, nullable=False)

    def get_id(self): #Função para pegar o identificador do usuário (necessário para login)
        return self.email

    def get_cpf(self):
        return self.cpf