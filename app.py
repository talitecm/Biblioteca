from flask import Flask, render_template, request, redirect, url_for, flash
from utilidades import * #Importando bando de dados.
from models.usuarios import * #importando a classe
import os #Biblioteca para ler arquivos como se fosse um "Sistema Operacional"
from dotenv import load_dotenv #Biblioteca para trabalhar com arquivos env
from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from datetime import datetime #importando uma forma de pegar a data atual
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
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') #Importando a secret key do flaskenv
lm.init_app(app) #Sinalizando que o loginManager será gerenciado pelo app
lm.login_view = 'login'  # Redireciona o usuário para a página de login caso não esteja autenticado

# Função para carregar o usuário
@lm.user_loader
def load_user(email):
    return Usuario.query.filter_by(email=email).first()  # Busca o usuário no banco pelo EMAIL

#Definindo rota login de usuário
@app.route('/', methods = ["get", "post"])
def login():
    return render_template("login.html")

#Excluir perfil do usuario
@app.route('/excluir_perfil', methods=['POST'])
@login_required
def excluir_perfil():
    # Obtendo o usuário atual
    usuario = current_user
    
    # Removendo o usuário do banco de dados
    db.session.delete(usuario)
    db.session.commit()
    
    # Deslogar o usuário
    logout_user()
    
    # Enviar uma mensagem de sucesso
    flash("Perfil excluído com sucesso!", "success")
    
    # Redirecionar para a página de login
    return redirect(url_for('login'))

#Definindo rota para verificar login do usuário
@app.route('/usuario_logado', methods = ["get", "post"])
def usuario_logado():
    email = request.form.get('email')
    senha = request.form.get('senha')
    usuario = load_user(email)
    
    if usuario == None: #Se o usuário não for encontrado
        msg = "Usuário não encontrado"
        return render_template("login.html", msg = msg)

    if usuario.email == email and usuario.senha == senha: # Se der certo
        login_user(usuario) #Efetua o login do usuário "iniciando uma sessão"
        return render_template("home.html", usuario = usuario)
    
    else: #Se o usuário for encontrado, mas o login falhar (erro de senha)
        msg = "Erro nas credenciais"
        return render_template("login.html", msg = msg)

#definindo rota para logout
@app.route('/logout', methods = ["get", "post"]) #Rota para deslogar usuário
@login_required #Sinalizando que o usuário só pode acessar essa página se fez o login
def logout():
    logout_user() #Função do pacote de login manager
    return redirect(url_for('login')) #redireciona para /login

#Definindo rota home
@app.route('/home', methods = ["get", "post"])
@login_required #Sinalizando que o usuário só pode acessar essa página se fez o login
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
    data_cad = datetime.now()

    novo_usuario = Usuario(nome=nome, cpf=cpf, endereco=endereco, email=email, senha=senha, data_cad=data_cad)
    
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
@app.route('/cadastrar_livros', methods = ["get", "post"])
def cadastrar_livro():
    return render_template("cadastrar_livros")
    
@app.route('/livro_cadastrado', methods=["POST"])
def livro_cadastrado():
    try:
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        ano = request.form.get('ano')

        # Conversão do ano para formato de data
        ano_lancamento = int(ano)

        # Criando o objeto Livro
        novo_livro = Livro(titulo=titulo, autor=autor, ano_lancamento=ano_lancamento)

        # Adicionando ao banco de dados
        db.session.add(novo_livro)
        db.session.commit()

        return redirect('catalogo.html')  # Redireciona para o catálogo de livros
    except Exception as e:
        return f"Erro ao cadastrar livro: {e}"

#Definindo rota para consultar livros
@app.route('/catalogo', methods = ["get", "post"])
def catalogo():
    return render_template("catalogo.html")

#Definindo rota para editar livros
@app.route('/editar_livros', methods = ["get", "post"])
def editar_livro():
    return render_template("editar_livros.html")

#Definindo rota para o perfil do usuário
@login_required #Sinalizando que o usuário só pode acessar essa página se fez o login
@app.route('/perfil_usuario', methods = ["get", "post"])
def perfil_usuario():
    return render_template("perfil_usuario.html")

@app.route('/editar_perfil', methods=['GET', 'POST'])
@login_required #Sinalizando que o usuário só pode acessar essa página se fez o login
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