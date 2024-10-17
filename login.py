from config_bd import criar_conexao
from os import system

def FazerLogin():
    print("------------------------")
    user = input("Digite seu username: ")
    senha = input("Digite sua senha: ")
    print("------------------------\n")

    conn = criar_conexao()

    
    cursor = conn.cursor()
    query = "SELECT username, senha FROM usuario WHERE username LIKE %s AND senha LIKE %s"
    cursor.execute(query, (user, senha,))
    retorno = cursor.fetchall()

    if retorno:
        print("Logado com sucesso!")
        cursor.close()
        conn.close()

    else:
        system('cls')
        print(f"Erro ao fazer o login! \n Tente novamente....\n")
        cursor.close()
        conn.close()
        FazerLogin()