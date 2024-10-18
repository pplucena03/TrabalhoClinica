from config_bd import criar_conexao


def BuscarEspecialidade(especialidade):
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

def BuscarPaciente(paciente):
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


def BuscarMedico(medico):
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


def ConsultarEspecialidade():
    conn = criar_conexao()

    try:
            cursor = conn.cursor()
            query = "SELECT nome FROM especialidade"
            cursor.execute(query)
            resultado = cursor.fetchall()
            
            print("\nEspecialidades cadastradas: ")
            for i in range(0, len(resultado)):
                print({resultado[i][0]})
            
                
    
            
            

    except Exception as e:
        print(f"Não foi possível buscar as especialidades: {e}")
    
    finally:
        cursor.close()
        conn.close()


def ConsultarMedico():
    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "SELECT medico.nome, crm, numero, especialidade.nome FROM medico INNER JOIN especialidade ON especialidade.id_especialidade = medico.id_especialidade"
        cursor.execute(query)
        resultado = cursor.fetchall()
        print(f"Médicos cadastrados: {resultado}") 

    except Exception as e:
        print(f"Não foi possível buscar os médicos: {e}")
    
    finally:
        cursor.close()
        conn.close()


def ConsultarPaciente():
    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "SELECT nome, data_nasc, sexo, telefone FROM paciente"
        cursor.execute(query)
        resultado = cursor.fetchall()
        print(f"Pacientes cadastrados: {resultado}") 

    except Exception as e:
        print(f"Não foi possível buscar os pacientes: {e}")
    
    finally:
        cursor.close()
        conn.close()


def ConsultarEndereco():
    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "SELECT rua, bairro, cidade, paciente.nome FROM endereco_paciente INNER JOIN paciente ON endereco_paciente.id_paciente = paciente.id_paciente"
        cursor.execute(query)
        resultado = cursor.fetchall()
        print(f"Endereços de pacientes cadastrados: {resultado}") 

    except Exception as e:
        print(f"Não foi possível buscar os endereços: {e}")
    
    finally:
        cursor.close()
        conn.close()