import os
from config_bd import criar_conexao
from consultar import BuscarEspecialidade, BuscarPaciente, BuscarMedico


def CadastroEspecialidade():
    especialidade = input("Digite o nome de uma especialidade: ").lower()
    conn = criar_conexao()   

    try:
        cursor = conn.cursor()
        query = "INSERT INTO especialidade (nome) VALUES (%s)"
        cursor.execute(query, (especialidade, ))
        conn.commit()
        print("Especialidade cadastrada com sucesso!")

        repetir = input("Deseja cadastrar outra? [S] ou [N]: ").lower()
        if repetir == 's':
            CadastroEspecialidade()
        elif repetir == 'n':
            pass
        else:
            print("Opção Invalida")

    except Exception as e:
        print(f"Erro ao cadastrar especialidade: {e}")

    finally:
        cursor.close()
        conn.close()

def CadastroMedico():       
    nome = input("Qual o nome do médico: ")
    crm = input(f"Qual o CRM do médico: ")
    data_nasc = input(f"Qual a data de nascimento do médico: ")
    sexo = input(f"Qual o sexo do médico: ")
    numero = input(f"Qual o numero do médico: ")
    especialidade = input(f"Qual a especialidade do médico: ")

    conn = criar_conexao()   
    id_especialidade = BuscarEspecialidade(especialidade)
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO medico (crm, data_nasc, id_especialidade, sexo, numero, nome) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (crm, data_nasc, id_especialidade, sexo, numero, nome))
        conn.commit()
        print("Médico cadastrado com sucesso!")

        repetir = input("Deseja cadastrar outro? [S] ou [N]: ").lower()
        if repetir == 's':
            CadastroMedico()

    except Exception as e:
        print(f"Erro ao cadastrar médico: {e}")
    finally:
        cursor.close()
        conn.close()

def CadastroPaciente():         
    nome = input("Qual o nome do paciente: ")
    data_nasc = input("Qual a data de nascimento do paciente(DD-MM-AAAA): ")
    sexo = input("Qual o sexo do paciente: ")
    telefone = input("Qual o numero do paciente: ")

    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "INSERT INTO paciente(data_nasc, sexo, telefone, nome) VALUES(%s, %s, %s, %s)"
        cursor.execute(query, (data_nasc, sexo, telefone, nome))
        conn.commit()
        print("Paciente cadastrado com sucesso")

        repetir = input("Deseja cadastrar outro? [S] ou [N]: ").lower()
        if repetir == 's':
            CadastroPaciente()
    
    except Exception as e:
        print(f"Erro ao cadastrar paciente: {e}") 
        
    finally:
        cursor.close()
        conn.close()
    
def CadastroEndereco():
    paciente = input("Qual o nome do paciente: ")
    rua = input("Qual a rua que o paciente mora: ")
    bairro = input("Qual bairro o paciente mora: ")
    cidade = input("Qual cidade o paciente mora: ")

    conn = criar_conexao()
    id_paciente = BuscarPaciente(paciente)

    try:
        cursor = conn.cursor()
        query = "INSERT INTO endereco_paciente(rua, bairro, cidade, id_paciente) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (rua, bairro, cidade, id_paciente))
        conn.commit()
    
    except Exception as e:
        print(f"Erro ao cadastrar o endereço do paciente: {e}")

    finally:
        cursor.close()
        conn.close()
        
def CadastroConsulta():

    paciente = input("Qual paciente será consultado: ")
    medico = input("Qual médico realizará a consulta: ")
    data = input("Qual será a data da consulta(DD-MM-AAAA): ")
    horario = input("Qual o horário da consulta(HH:MM): ")

    conn = criar_conexao()
    
    id_paciente = BuscarPaciente(paciente)
    id_medico = BuscarMedico(medico)

    try:
        cursor = conn.cursor()
        query = "INSERT INTO consulta(data, horario, id_medico, id_paciente) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data, horario, id_medico, id_paciente))
        conn.commit()
    
    except Exception as e:
        print(f"Erro ao agendar consulta: {e}")

    finally:
        cursor.close()  

def CadastrarUsuario():
    user = input("Digite um username: ")
    senha = input("Digite uma senha: ")

    conn = criar_conexao()

    cursor = conn.cursor()
    query = "SELECT username, senha FROM usuario WHERE username LIKE %s AND senha LIKE %s"
    cursor.execute(query, (user, senha,))
    retorno = cursor.fetchall()

    if retorno:
        print("Já existe um usuário com esse username e senha!\n Tente novamente...")
        CadastrarUsuario()
    else:
        try:
            query = "INSERT INTO usuario(username, senha) VALUES(%s, %s)"
            cursor.execute(query, (user, senha,))
            conn.commit()
            print("Usuário cadastrado com sucesso!")
        
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")
        
        finally:
            cursor.close()
            conn.close()
            
        return True