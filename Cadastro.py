import os
from config_bd import criar_conexao
from consultar import buscar_especialidade, buscar_paciente, buscar_medico


def cadastro_especialidade():
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
            cadastro_especialidade()
        elif repetir == 'n':
            pass
        else:
            print("Opção Invalida")

    except Exception as e:
        print(f"Erro ao cadastrar especialidade: {e}")

    finally:
        cursor.close()
        conn.close()

def cadastro_medico():       
    nome = input("Qual o nome do médico: ")
    crm = input(f"Qual o CRM do médico: ")
    data_nasc = input(f"Qual a data de nascimento do médico: ")
    sexo = input(f"Qual o sexo do médico: ")
    numero = input(f"Qual o numero do médico: ")
    especialidade = input(f"Qual a especialidade do médico: ")

    conn = criar_conexao()   
    id_especialidade = buscar_especialidade(especialidade)
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO medico (crm, data_nasc, id_especialidade, sexo, numero, nome) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (crm, data_nasc, id_especialidade, sexo, numero, nome))
        conn.commit()
        print("Médico cadastrado com sucesso!")

        repetir = input("Deseja cadastrar outro? [S] ou [N]: ").lower()
        if repetir == 's':
            cadastro_medico()

    except Exception as e:
        print(f"Erro ao cadastrar médico: {e}")
    finally:
        cursor.close()
        conn.close()

def cadastro_paciente():         
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
            cadastro_paciente()
    
    except Exception as e:
        print(f"Erro ao cadastrar paciente: {e}") 
        
    finally:
        cursor.close()
        conn.close()
    
def cadastro_endereco():
    paciente = input("Qual o nome do paciente: ")
    rua = input("Qual a rua que o paciente mora: ")
    bairro = input("Qual bairro o paciente mora: ")
    cidade = input("Qual cidade o paciente mora: ")

    conn = criar_conexao()
    id_paciente = buscar_paciente(paciente)

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
        
def cadastro_consulta():

    paciente = input("Qual paciente será consultado: ")
    medico = input("Qual médico realizará a consulta: ")
    data = input("Qual será a data da consulta(DD-MM-AAAA): ")
    horario = input("Qual o horário da consulta(HH:MM): ")

    conn = criar_conexao()
    
    id_paciente = buscar_paciente(paciente)
    id_medico = buscar_medico(medico)

    try:
        cursor = conn.cursor()
        query = "INSERT INTO consulta(data, horario, id_medico, id_paciente) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data, horario, id_medico, id_paciente))
        conn.commit()
    
    except Exception as e:
        print(f"Erro ao agendar consulta: {e}")

    finally:
        cursor.close()  