from config_bd import criar_conexao
from os import system
import bcrypt

def fazer_login(user, senha):
    conn = criar_conexao()
    cursor = conn.cursor()
    query = "SELECT username, senha FROM usuario WHERE username = %s"
    cursor.execute(query, (user,))
    retorno = cursor.fetchall()

    if len(retorno) > 0:
        if isinstance(retorno[0][1], memoryview):
            hashed_password = bytes(retorno[0][1])

        if check_senha(senha, hashed_password):
            print("Logado com sucesso!")
            cursor.close()
            conn.close()
            return False

    system('cls')
    print("Erro ao fazer o login! \n Tente novamente....\n")
    cursor.close()
    conn.close()
    return True


def cadastro_usuario(user, senha):
    senha = criptografar(senha)

    conn = criar_conexao()
    cursor = conn.cursor()
    query = "SELECT username FROM usuario WHERE username = %s"
    cursor.execute(query, (user,))
    retorno = cursor.fetchall()

    if retorno:
        system('cls')
        print("Já existe um usuário com esse username!\n Tente novamente...")
        return True
        
    else:
        try:
            query = "INSERT INTO usuario(username, senha) VALUES(%s, %s)"
            cursor.execute(query, (user, senha,))
            conn.commit()
            print("Usuário cadastrado com sucesso!")
            return False
        
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")
            cursor.close()
            conn.close()
            return True


def criptografar(senha):
    bytes = senha.encode('utf-8')
    hashed = bcrypt.hashpw(bytes, bcrypt.gensalt(14))
    return hashed
   
   
def check_senha(senha, hashed):
    bytes = senha.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed)