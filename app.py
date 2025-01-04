from flask import Flask, render_template, request, redirect, url_for
from utilidades import * #Importando bando de dados.
from models.usuarios import * #importando a classe
import os #Biblioteca para ler arquivos como se fosse um "Sistema Operacional"
from dotenv import load_dotenv #Biblioteca para trabalhar com arquivos env
from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional

app = Flask(__name__)

load_dotenv() #Carrega variáveis do nosso arquivo .flaskenv

dbusuario = os.getenv("DB_USERNAME") #Importando informação de usuário do arquivo env
dbsenha = os.getenv("DB_PASSWORD") #Importando informação de senha do arquivo env
host = os.getenv("DB_HOST") #Importando informação de host do arquivo env
meubanco = os.getenv("DB_DATABASE") #Importando informação de banco de dados do arquivo env
porta = os.getenv("DB_PORT") #importando a informação da porta da conexão do arquivo env
conexao = f"mysql+pymysql://{dbusuario}:{dbsenha}@{host}:{porta}/{meubanco}" #Formatando a linha de conexão com o banco
app.config["SQLALCHEMY_DATABASE_URI"] = conexao #Criando uma "rota" de comunicação
db.init_app(app) #Sinaliza que o banco será gerenciado pelo app

#Definindo rota login de usuário
@app.route('/')
def login():
    return render_template("login.html")

#Definindo rota home
@app.route('/home')
def home():
    return render_template("home.html")

#Definindo rota registro de usuário
@app.route('/registrar_usuario', methods = ["get","post"])
def registro():
    return render_template("registrar_usuario.html")

#Definindo rota para Usuário cadastrado
@app.route('/usuario_cadastrado', methods = ["get","post"])
def usuario_cadastrado():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    endereco = request.form.get('endereco')
    email = request.form.get('email')
    senha = request.form.get('senha')

    novo_usuario = Usuario(nome=nome, cpf=cpf, endereco=endereco, email=email, senha=senha)
    
    db.session.add(novo_usuario)
    db.session.commit()

    return render_template("login.html", usuario=novo_usuario)

#Definindo rota sobre
@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

#Definindo rota contato
@app.route('/contato')
def contato():
    return render_template("contato.html")

#Definindo rota para cadastrar livros
@app.route('/cadastrar_livros')
def cadastrar_livro():
    return render_template("cadastrar_livros.html")

#Definindo rota para consultar livros
@app.route('/catalogo')
def catalogo():
    return render_template("catalogo.html")

#Definindo rota para editar livros
@app.route('/editar_livros')
def editar_livro():
    return render_template("editar_livros.html")

#Definindo rota para o perfil do usuário
@app.route('/perfil_usuario')
def perfil_usuario():
    return render_template("perfil_usuario.html")

@app.route('/editar_perfil', methods=['GET', 'POST'])
def editar_perfil():
    if request.method == 'POST':
        # Aqui você pode salvar as informações atualizadas no banco de dados
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        senha = request.form['senha']

        # Retorna à página de perfil do usuário
        return redirect(url_for('perfil_usuario'))

    return render_template('editar_perfil.html')