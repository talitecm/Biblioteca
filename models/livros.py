from utilidades import *
#from flask_login import UserMixin

class Livro(db.Model):
    __tablename__="livros"
    idlivro = db.Column(db.Integer, primary_key = True, autoincrement = True)
    titulo = db.Column(db.String(45), nullable=False)
    autor = db.Column(db.String(45), nullable=False)
    ano_lancamento = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(50))
    senha = db.Column(db.String(15))    

    def get_id(self): #Função para pegar o identificador do usuário (necessário para login)
        return self.cpf