from flask import Flask, render_template, request

app = Flask(__name__)

#Definindo rota inicial
@app.route('/')
def inicio():
    return render_template("index.html")

#Definindo rota registro de usuário
@app.route('/registrar_usuario')
def registro():
    return render_template("registrar_usuario.html")

#Definindo rota login de usuário
@app.route('/login')
def login():
    return render_template("login.html")

#Definindo rota para cadastrar livros
@app.route('/cadastrar_livros')
def cadastrar_livro():
    return render_template("cadastrar_livros.html")

#Definindo rota para reservar livros
@app.route('/reservar_livros')
def reservar_livro():
    return render_template("reservar_livros.html")

#Definindo rota para editar livros
@app.route('/editar_livros')
def editar_livro():
    return render_template("editar_livros.html")

#Definindo rota para remover livros
@app.route('/remover_livros')
def remover_livro():
    return render_template("remover_livros.html")
