from config_bd import criar_conexao
from consultar import buscar_especialidade, buscar_paciente

def editar_medico():
    nome_inicial = input("Digite o nome do médico que deseja editar: ")

    conn = criar_conexao()

    cursor = conn.cursor()
    query = "SELECT nome FROM medico WHERE nome ILIKE %s"
    cursor.execute(query, (nome_inicial,))
    busca = cursor.fetchone()
    
    if busca:
        print(f"Médico encontrado! Digite os novos dados de {busca[0]}\n")

    else:
        print(f"Não foi possível encontrar o médico\n Tente novamente....\n")
        editar_medico()

    cursor.close()

    nome = input("Qual o nome do médico: ")
    crm = input(f"Qual o CRM do médico: ")
    data_nasc = input(f"Qual a data de nascimento do médico: ")
    sexo = input(f"Qual o sexo do médico: ")
    numero = input(f"Qual o numero do médico: ")
    especialidade = input(f"Qual a especialidade do médico: ")

    id_especialidade = buscar_especialidade(especialidade)

    try:
        cursor = conn.cursor()
        query = "UPDATE medico SET crm = %s, data_nasc = %s, id_especialidade = %s, sexo = %s, numero = %s, nome = %s WHERE nome ILIKE %s"
        cursor.execute(query, (crm, data_nasc, id_especialidade, sexo, numero, nome, nome_inicial))
        conn.commit()
        print("Médico atualizado com sucesso!")

        repetir = input("Deseja editar outro? [S] ou [N]: ").lower()
        if repetir == 's':
            editar_medico()

    except Exception as e:
        print(f"Erro ao editar o médico: {e}")
    finally:
        cursor.close()
        conn.close()

def editar_paciente():
    nome_inicial = input("Digite o nome do paciente que deseja editar: ")

    conn = criar_conexao()

    try:
        cursor = conn.cursor()
        query = "SELECT nome FROM paciente WHERE nome ILIKE %s"
        cursor.execute(query, (nome,))
        busca = cursor.fetchone()
        
        if busca:
            print(f"Paciente encontrado! Digite os novos dados de {busca[0]}\n")

    except Exception as e:
        print(f"Não foi possível encontrar o paciente: {e}")

    finally:
        cursor.close()

    nome = input("Qual o nome do paciente: ")
    data_nasc = input("Qual a data de nascimento do paciente(DD-MM-AAAA): ")
    sexo = input("Qual o sexo do paciente: ")
    telefone = input("Qual o numero do paciente: ")

    try:
        cursor = conn.cursor()
        query = "UPDATE paciente SET nome = %s, data_nasc = %s, sexo = %s, telefone = %s WHERE nome ILIKE %s"
        cursor.execute(query, (nome, data_nasc, sexo, telefone, nome_inicial))
        conn.commit()
        print("Paciente atualizado com sucesso!")

        repetir = input("Deseja editar outro? [S] ou [N]: ").lower()
        if repetir == 's':
            editar_paciente()

    except Exception as e:
        print(f"Erro ao editar o paciente: {e}")
    finally:
        cursor.close()
        conn.close()

def editar_endereco():
    paciente = input("Digite o nome do paciente que deseja editar o endereço: ")
    id_paciente = buscar_paciente(paciente)
    
    conn = criar_conexao()

    rua = input("Qual a rua que o paciente mora: ")
    bairro = input("Qual bairro o paciente mora: ")
    cidade = input("Qual cidade o paciente mora: ")

    try:
        cursor = conn.cursor()
        query = "UPDATE endereco_paciente SET rua = %s, bairro = %s, cidade = %s WHERE id_paciente = %s"
        cursor.execute(query, (rua, bairro, cidade, id_paciente))
        conn.commit()
        print("Endereço atualizado com sucesso!")

        repetir = input("Deseja editar outro? [S] ou [N]: ").lower()
        if repetir == 's':
            editar_endereco()

    except Exception as e:
        print(f"Erro ao editar o endereço: {e}")
    finally:
        cursor.close()
        conn.close()