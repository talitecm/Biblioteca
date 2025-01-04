from utilidades import *
#from flask_login import UserMixin

class Usuario(db.Model):
    __tablename__="usuario"
    id_usuario = db.Column(db.int(35))
    nome_usuario = db.Column(db.String(100), nullabel=False)
    email_usuario = db.Column(db.String(50), nullabel=False)
    senha_usuario = db.Column(db.String(15), nullabel=False)
    endereco_usuario = db.Column(db.String(50), nullabel=False)
    cpf = db.Column(db.String(11), primary_key = True)

    def get_id(self): #Função para pegar o identificador do usuário (necessário para login)
        return self.cpf