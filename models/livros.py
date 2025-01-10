from flask_login import UserMixin
from utilidades import *
from flask_sqlalchemy import SQLAlchemy


class Livro(db.Model):
    __tablename__ = "livros"
    idlivro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(45), nullable=False)
    autor = db.Column(db.String(45), nullable=False)
    ano_lancamento = db.Column(db.Date, nullable=False)
    isbn = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<Livro {self.titulo} - {self.autor}>"
