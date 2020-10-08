"""
Como vimos em aula, este é um serviço WEB, que recebe requisições HTTP e envia as
respostas caso a rota seja reconhecida, se a rota não for reconhecida o o framework
Flask retorna o erro 404 NOT FOUND automaticamente.

Para rodar o programa digite...

$ python3 app.py

experimente então no Browser as rotas definidas, se a rota tiver <algum_nome>,
a função vinculada a rota deve ter como parâmetro uma variável com o o mesmo nome,
(veja a rota de comentários) e você terá acesso ao valor que foi passado nesta variável.

Tente criar novas rotas com elementos referentes a um sistema de blogs, como curtidas em
posts e comentários, grupos, etc.

Caso tenham dúvidas usem o nosso grupo do Discord ou enviem um e-mail para
msbrito@uesc.br.
"""
import json
from flask import Flask
from flask import request
import usuario
import dataset


app = Flask(__name__)

db = dataset.connect('mysql://root@localhost/blogsd')

@app.route('/')
def home():
    return 'Bem vindo ao blog!'


@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'GET':
        return usuario.lista_usuarios(db)
    else:
        return usuario.cadastra_usuario(db, request.json)



@app.route('/posts')
def posts():
    return json.dumps(['Post X', 'Post Y'])


@app.route('/posts/<id>')
def detalhes_do_posts(id):
    return f'Detalhes do Post {id}'


@app.route('/posts/<id>/comentarios')
def hello(id):
    return f'<a href="#">Comentários do Post {id}</a>'


if __name__ == '__main__':
    app.run()
