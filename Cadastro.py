import os
from config_bd import criar_conexao

def CadastroEspecialidade():
    while(True):
        especialidade = input("Digite o nome de uma especialidade: ").lower()
        conn = criar_conexao()   

        try:
            cursor = conn.cursor()
            query = "INSERT INTO Especialidade (nome) VALUES (%s);"
            cursor.execute(query, (especialidade))
            conn.commit()
            print("Especialidade cadastrada com sucesso!")

            repetir = input("Deseja cadastrar outra? [S] ou [N]: ").lower()
            if repetir == 's':
                CadastroEspecialidade()

        except Exception as e:
            print(f"Erro ao cadastrar especialidade: {e}")

        finally:
            cursor.close()
            conn.close()
            break
    
    return True

def CadastroMedico():       
    nome = input("Qual o nome do médico: ")
    crm = input(f"Qual o CRM do médico: ")
    data_nasc = input(f"Qual a data de nascimento do médico: ")
    sexo = input(f"Qual o sexo do médico: ")
    numero = input(f"Qual o numero do médico: ")
    especialidade = input(f"Qual a especialidade do médico: ").lower()

    conn = criar_conexao()   
    try: 
        cursor = conn.cursor()
        query = "SELECT id_especialidade FROM especialidade WHERE nome LIKE '%s'"
        cursor.execute(query, especialidade)
        id_especialidade = cursor.fetchall()
    except:
        print("Especialidade não encontrada")
    finally:
        cursor.close()
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO especialidade (crm, data_nasc, id_especialidade, sexo, numero, nome) VALUES (%s, %s, %s, %s, %s, %s);"
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
    nome_paciente = input("Qual o nome do paciente: ")
    data_paciente = input("Qual a data de nascimento do paciente: ")
    sexo_paciente = input("Qual o sexo do paciente: ")
    telefone = input("Qual o numero do paciente: ")
        
            
def CadastroEndereco():
    os.system('cls')
    rua = input("Qual a rua que o paciente mora: ")
    bairro = input("Qual bairro o paciente mora: ")
    cidade = input("Qual cidade o paciente mora: ")
                
     