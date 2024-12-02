from config_bd import criar_conexao
import time


def buscar_especialidade(especialidade):
    conn = criar_conexao()
      
    try:
        cursor = conn.cursor()
        query = "SELECT id_especialidade FROM especialidade WHERE nome ILIKE %s"
        cursor.execute(query, (especialidade,))
        id_especialidade = cursor.fetchone()
    except:
        print("Especialidade não encontrada")
    finally:
        cursor.close()
        conn.close()

    return id_especialidade[0]

def buscar_paciente(paciente):
    conn = criar_conexao()
      
    try:
        cursor = conn.cursor()
        query = "SELECT id_paciente FROM paciente WHERE nome ILIKE %s"
        cursor.execute(query, (paciente,))
        id_paciente = cursor.fetchone()
    except:
        print("Paciente não encontrado(a)")
    finally:
        cursor.close()
        conn.close()

    return id_paciente[0]


def buscar_medico(medico):
    conn = criar_conexao()
      
    try:
        cursor = conn.cursor()
        query = "SELECT id_medico FROM medico WHERE nome ILIKE %s"
        cursor.execute(query, (medico,))
        id_medico = cursor.fetchone()
    except:
        print("Médico não encontrado(a)")
    finally:
        cursor.close()
        conn.close()

    return id_medico[0]


def consultar_especialidade():
    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "SELECT nome FROM especialidade"
        cursor.execute(query)
        resultado = cursor.fetchall()
        
        print("\nEspecialidades cadastradas: ")
        for i in range(0, len(resultado)):
            print({resultado[i][0]})

        print("Precione Enter para continuar...")
        input()

    except Exception as e:
        print(f"Não foi possível buscar as especialidades: {e}")
    
    finally:
        cursor.close()
        conn.close()


def consultar_medico():
    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "SELECT medico.nome, crm, numero, especialidade.nome FROM medico INNER JOIN especialidade ON especialidade.id_especialidade = medico.id_especialidade"
        cursor.execute(query)
        resultado = cursor.fetchall()
        print("----- Médicos cadastrados -----")
        for i in range(0, len(resultado)):
            print(f"Nome: {resultado[i][0]} \nCRM: {resultado[i][1]} \nNúmero: {resultado[i][2]} \nEspecialidade: {resultado[i][3]} \n-------------") 
        print("Precione Enter para continuar...")
        input()

    except Exception as e:
        print(f"Não foi possível buscar os médicos: {e}")
    
    finally:
        cursor.close()
        conn.close()


def consultar_paciente():
    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "SELECT nome, data_nasc, sexo, telefone FROM paciente"
        cursor.execute(query)
        resultado = cursor.fetchall()
        print("\n--- Pacientes cadastrados ---")
        for i in range(0, len(resultado)):
            print(f"Nome: {resultado[i][0]} \nData de Nascimento: {resultado[i][1]} \nSexo: {resultado[i][2]} \nTelefone: {resultado[i][3]} \n-------------") 
        
        print("Precione Enter para continuar...")
        input()

    except Exception as e:
        print(f"Não foi possível buscar os pacientes: {e}")
    
    finally:
        cursor.close()
        conn.close()


def consultar_endereco():
    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "SELECT rua, bairro, cidade, paciente.nome FROM endereco_paciente INNER JOIN paciente ON endereco_paciente.id_paciente = paciente.id_paciente"
        cursor.execute(query)
        resultado = cursor.fetchall()
        print("---- Endereços de pacientes cadastrados ----\n")
        for i in range(0, len(resultado)):
            print(f"Rua: {resultado[i][0]} \nBairro: {resultado[i][1]} \nCidade: {resultado[i][2]} \nPaciente: {resultado[i][3]} \n---------------\n")

        opcao =  input("Deseja realizar mais alguma ação? [S] ou [N]: ").lower()
        if opcao == 's':
            time.sleep(1)
            pass
        elif opcao == 'n':
            exit()
        else:
            print("\nOpção inválida!")
            time.sleep(1)
            pass 

    except Exception as e:
        print(f"Não foi possível buscar os endereços: {e}")
    
    finally:
        cursor.close()
        conn.close()