from utilidades import db

class Usuario(db.Model):
    __tablename__="usuario"
    id_usuario = db.Column(db.String(35),primary_key = True)
    nome_usuario = db.Column(db.String(35))
    email_usuario = db.Column(db.String(50))
    senha_usuario = db.Column(db.String(8))
    endereco_usuario = db.Column(db.String(8))
    cpf_usuario = db.Column(db.String(8))

    def __init__(self, nome_usuario, email_usuario, senha_usuario, endereco_usuario, cpf_usuario):
        self.animalname = animalname
        self.animallocalization = animallocalization
        self.animaltype = animaltype