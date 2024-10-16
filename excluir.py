from config_bd import criar_conexao
from consultar import ConsultarEspecialidade, ConsultarMedico, ConsultarPaciente, ConsultarEndereco, BuscarPaciente

def ExcluirEspecialidade():
    ConsultarEspecialidade()
    especialidade = input("\nDigite a especialidade que deseja excluir: ")

    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "DELETE FROM especialidade WHERE nome ILIKE %s"
        cursor.execute(query, (especialidade,))
        print(f"{especialidade} excluída com sucesso!")
    
    except Exception as e:
        print(f"Erro ao excluir especialidade: {e}")

    finally:
        cursor.close()
        conn.close()

def ExcluirMedico():
    ConsultarMedico()
    medico = input("\nDigite o nome do médico que deseja excluir: ")

    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "DELETE FROM medico WHERE nome ILIKE %s"
        cursor.execute(query, (medico,))
        print(f"{medico} excluído(a) com sucesso!")
    
    except Exception as e:
        print(f"Erro ao excluir médico: {e}")

    finally:
        cursor.close()
        conn.close()
        
def ExcluirPaciente():
    ConsultarPaciente()
    paciente = input("\nDigite o nome do paciente que deseja excluir: ")
    id_paciente = BuscarPaciente(paciente)
    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "DELETE FROM endereco_paciente WHERE id_paciente = %s"
        cursor.execute(query, (id_paciente,))
        print("Excluíndo dados do paciente....")

    except Exception as e:
        print(f"Erro ao excluir dados do endereço do paciente: {e}")
    
    finally:
        cursor.close()

    try:
        cursor = conn.cursor()
        query = "DELETE FROM paciente WHERE nome ILIKE %s"
        cursor.execute(query, (paciente,))
        print(f"{paciente} excluído(a) com sucesso!")
    
    except Exception as e:
        print(f"Erro ao excluir paciente: {e}")

    finally:
        cursor.close()
        conn.close()

def ExcluirEndereco():
    ConsultarEndereco()
    endereco = input("\nDigite o nome do paciente referente ao endereço que deseja excluir: ")
    id_paciente = BuscarPaciente(endereco)

    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "DELETE FROM endereco WHERE id_paciente ILIKE %s"
        cursor.execute(query, (id_paciente,))
        print("Endereço excluído com sucesso!")
    
    except Exception as e:
        print(f"Erro ao excluir especialidade: {e}")

    finally:
        cursor.close()
        conn.close()