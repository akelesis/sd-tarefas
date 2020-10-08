def lista_usuarios(db):
    users = {}
    index = 0
    for user in db['usuario']:
        nome = user['nome']
        login = user['login']
        senha = user['senha']
        users[index] = dict(nome=nome, login=login, senha=senha)
        index = index + 1
    return users

def cadastra_usuario(db, usuario):
    user = db['usuario']

    user.insert(dict(nome=usuario["nome"], login=usuario["login"], senha=usuario["senha"]))

    return "Created Successfully", 201
