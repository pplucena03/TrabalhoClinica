from config_bd import criar_conexao
from consultar import consultar_especialidade, consultar_medico, consultar_paciente, consultar_endereco, buscar_paciente, buscar_medico

def excluir_especialidade():
    consultar_especialidade()
    especialidade = input("\nDigite a especialidade que deseja excluir: ")

    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "DELETE FROM especialidade WHERE nome ILIKE %s"
        cursor.execute(query, (especialidade,))
        conn.commit()
        print(f"{especialidade} excluída com sucesso!")
    
    except Exception as e:
        print(f"Erro ao excluir especialidade: {e}")

    finally:
        cursor.close()
        conn.close()

def excluir_medico():
    medico = input("\nDigite o nome do médico que deseja excluir: ")
    #id_medico = buscar_medico(medico)

    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "DELETE FROM medico WHERE nome LIKE %s"
        cursor.execute(query, (medico,))
        conn.commit()
        print(f"{medico} excluído(a) com sucesso!")
    
    except Exception as e:
        print(f"Erro ao excluir médico: {e}")

    finally:
        cursor.close()
        conn.close()
        
def excluir_paciente():
    consultar_paciente()
    paciente = input("\nDigite o nome do paciente que deseja excluir: ")
    id_paciente = buscar_paciente(paciente)
    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "DELETE FROM endereco_paciente WHERE id_paciente = %s"
        cursor.execute(query, (id_paciente,))
        conn.commit()
        print("Excluíndo dados do paciente....")

    except Exception as e:
        print(f"Erro ao excluir dados do endereço do paciente: {e}")
    
    finally:
        cursor.close()

    try:
        cursor = conn.cursor()
        query = "DELETE FROM paciente WHERE nome LIKE %s"
        cursor.execute(query, (paciente,))
        conn.commit()
        print(f"{paciente} excluído(a) com sucesso!")
    
    except Exception as e:
        print(f"Erro ao excluir paciente: {e}")

    finally:
        cursor.close()
        conn.close()

def excluir_endereco():
    consultar_endereco()
    endereco = input("\nDigite o nome do paciente referente ao endereço que deseja excluir: ")
    id_paciente = buscar_paciente(endereco)

    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "DELETE FROM endereco WHERE id_paciente ILIKE %s"
        cursor.execute(query, (id_paciente,))
        conn.commit()
        print("Endereço excluído com sucesso!")
    
    except Exception as e:
        print(f"Erro ao excluir especialidade: {e}")

    finally:
        cursor.close()
        conn.close()